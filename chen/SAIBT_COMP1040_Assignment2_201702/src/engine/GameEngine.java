package engine;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.HashSet;

import javax.swing.JFrame;
import javax.swing.Timer;

import engine.graphics.GraphicsWindow;
import engine.input.Keyboard;
import engine.input.Mouse;
import engine.interfaces.ICollidable;
import engine.interfaces.IPaintable;
import engine.interfaces.IUpdatable;

/**
 * The GameEngine keeps track of all objects implementing IPaintable, 
 * IUpdatable and ICollidable. It will automatically call each 
 * object's update, onCollision and paint methods 60 times per 
 * second.
 * 
 * Each object may be added to the GameEngine using GameEngine.add().
 * A Game must be added to the GameEngine using 
 * GameEngine.loadGame(g); this will automatically call the Game 
 * object's load() method and then display the window to the size 
 * returned from that Game's getWindowWidth() and getWindowHeight() 
 * methods.
 * 
 * @author Michael
 *
 */
public class GameEngine{

	private static Mouse mouse;
	private static Keyboard keyboard;
	private static GraphicsWindow mainWindow;
	private static Game game;

	private static final ArrayList<IPaintable> backgroundPaintObjects = new ArrayList<IPaintable>();
	private static final ArrayList<IPaintable> paintObjects = new ArrayList<IPaintable>();
	private static final ArrayList<IPaintable> guiObjects = new ArrayList<IPaintable>();
	private static final ArrayList<IUpdatable> updateObjects = new ArrayList<IUpdatable>();
	private static final ArrayList<ICollidable> collidableObjects = new ArrayList<ICollidable>();

	private static long lastTime;
	private static boolean debug = false;	
	private static boolean paused = false;

	/**
	 * private constructor makes this a singleton.
	 */
	private GameEngine(){ }

	/**
	 * This static block executes as the first reference to
	 * GameEngine is made. It creates the mainWindow, keyboard 
	 * and mouse objects.
	 */
	static{
		GameEngine.mainWindow = new GraphicsWindow();
		GameEngine.mainWindow.setDefaultCloseOperation(
				JFrame.EXIT_ON_CLOSE);

		GameEngine.keyboard = Keyboard.instance;
		GameEngine.mainWindow.addKeyboard(GameEngine.keyboard);

		GameEngine.mouse = Mouse.instance;
		GameEngine.mainWindow.addMouse(GameEngine.mouse);
	}

	/**
	 * Sets up the update and paint timers and starts them running.
	 */
	private static void run(){	
		GameEngine.lastTime = System.nanoTime();
		Timer updateTimer = new Timer(1000/60, new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent event){
				GameEngine.autoUpdate(
						(System.nanoTime() - lastTime)/1000000);
				GameEngine.lastTime = System.nanoTime();
			}
		});

		Timer paintTimer = new Timer(1000/60, new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent event) {
				repaint();
			}
		});

		paintTimer.start();
		updateTimer.start();
	}

	/**
	 * Exits the program. This closes the window and ends the Java 
	 * application.
	 */
	public static void quit(){
		System.exit(0);
	}

	/**
	 * Automatically calls the mouse, keyboard, mainWindow and Game 
	 * update methods. Also calls the update method of any IUpdatable 
	 * objects that have been added to the GameEngine, provided the 
	 * GameEngine is not paused. This is automatically called 
	 * approximately 60 times per second.
	 * @param millisElapsed the milliseconds since the last call to 
	 * this method. This is passed to each update method so that 
	 * actions can be scaled by time passed instead of frames per 
	 * second.
	 */
	private static void autoUpdate(long millisElapsed){
		GameEngine.mouse.update(millisElapsed);
		GameEngine.keyboard.update(millisElapsed);
		GameEngine.mainWindow.update(millisElapsed);

		if(!GameEngine.paused){
			GameEngine.update(millisElapsed);
		}
	}

	/**
	 * This will call the update method of the Game and any 
	 * IUpdatable objects that have been added to the GameEngine. 
	 * It will also call the collision methods of any ICollidable 
	 * objects that have been added to the GameEngine.
	 * @param millisElapsed the milliseconds since the last call to 
	 * this method. This is passed to each update method so that 
	 * actions can be scaled by time passed instead of frames per 
	 * second. 
	 */
	public static void update(long millisElapsed){
		GameEngine.game.update(millisElapsed);

		for(int i=updateObjects.size()-1; i>=0; i--){
			updateObjects.get(i).update(millisElapsed);
		}
		for(int i=0; i<GameEngine.collidableObjects.size(); i++){
			for(int j=0; j<GameEngine.collidableObjects.size(); j++){
				if(i != j){
					if(GameEngine.collidableObjects.get(i).collidedWith(
							GameEngine.collidableObjects.get(j))){
						GameEngine.collidableObjects.get(i).onCollision(
								GameEngine.collidableObjects.get(j));
					}
					else if(GameEngine.collidableObjects.get(j).collidedWith(
							GameEngine.collidableObjects.get(i))){
						GameEngine.collidableObjects.get(j).onCollision(
								GameEngine.collidableObjects.get(i));
					}
				}
			}
		}
	}

	/**
	 * refreshes the graphics in the MainWindow, therefore showing 
	 * each Game Object at its correct position on the screen.
	 */
	public static void repaint(){
		mainWindow.repaint();
	}	

	/**
	 * The given object must be a subclass of IUpdatable, IPaintable 
	 * and/or ICollidable. If it is, the object will be added to the 
	 * GameEngine's internal data structure. It will then be 
	 * automatically managed and processed by the update and paint 
	 * timers.
	 * 
	 * If it is an IPaintable, its paint method will be called;
	 * if it is an IUpdatable, its update method will be called; 
	 * if it is an ICollidable, its collided and onCollision methods 
	 * will be called. 
	 * 
	 * This method only needs to be called once for each object, even 
	 * if that object implements more than one of the interfaces.
	 * @param obj an object implementing either IUpdatable, ICollidable 
	 * or IUpdatable.
	 * @throws ClassCastException if the object does not implement 
	 * IUpdatable, IPaintable or ICollidable.
	 */
	public static void add(Object obj) throws ClassCastException{
		if(obj instanceof IUpdatable){
			if(!GameEngine.updateObjects.contains(obj)){
				GameEngine.updateObjects.add((IUpdatable)obj);
			}
		}
		if(obj instanceof IPaintable){
			if(!GameEngine.paintObjects.contains(obj)){
				GameEngine.paintObjects.add((IPaintable)obj);
			}
		}
		if(obj instanceof ICollidable){
			if(!GameEngine.collidableObjects.contains(obj)){
				GameEngine.collidableObjects.add((ICollidable)obj);
			}
		}
		if(!(obj instanceof IUpdatable) && !(obj instanceof IPaintable) 
				&& !(obj instanceof ICollidable)){
			throw new ClassCastException(obj + 
					" does not implement IUpdatable, IPaintable or "
					+ "ICollidable");
		}
	}

	/**
	 * Performs the same function as add(Object o) but the object 
	 * will be painted on top of any other IPaintables. The given 
	 * object must implement IPaintable but may also implement the 
	 * IUpdatable and ICollidable interfaces. This method only needs
	 * to be called once for each object, even if that object 
	 * implements more than one interface. If you are calling this 
	 * method, you do not also need to call the add(Object o) method.
	 * @param obj an object implementing the IPaintable interface. 
	 * @throws ClassCastException if the object does not implement 
	 * IUpdatable, IPaintable or ICollidable.
	 */
	public static void addToGUI(IPaintable obj) 
			throws ClassCastException{
		if(obj instanceof IUpdatable){
			if(!GameEngine.updateObjects.contains(obj)){
				GameEngine.updateObjects.add((IUpdatable)obj);
			}
		}
		if(obj instanceof IPaintable){
			if(!GameEngine.guiObjects.contains(obj)){
				GameEngine.guiObjects.add((IPaintable)obj);
			}
		}
		if(obj instanceof ICollidable){
			if(!GameEngine.collidableObjects.contains(obj)){
				GameEngine.collidableObjects.add((ICollidable)obj);
			}
		}
		if(!(obj instanceof IUpdatable) && !(obj instanceof IPaintable) 
				&& !(obj instanceof ICollidable)){
			throw new ClassCastException(obj + 
					" does not implement IUpdatable, IPaintable or "
					+ "ICollidable");
		}
	}

	/**
	 * Performs the same function as add(Object o) but the object 
	 * will be painted behind any other IPaintables. The given object 
	 * must implement IPaintable but may also implement the 
	 * IUpdatable and ICollidable interfaces. This method only needs 
	 * to be called once for each object, even if that object 
	 * implements more than one interface. If you are calling this 
	 * method, you do not also need to call the add(Object o) method.
	 * @param obj an object implementing the IPaintable interface. 
	 * @throws ClassCastException if the object does not implement 
	 * IUpdatable, IPaintable or ICollidable.
	 */
	public static void addToBackground(IPaintable obj) 
			throws ClassCastException{
		if(obj instanceof IUpdatable){
			if(!GameEngine.updateObjects.contains(obj)){
				GameEngine.updateObjects.add((IUpdatable)obj);
			}
		}
		if(obj instanceof IPaintable){
			if(!GameEngine.backgroundPaintObjects.contains(obj)){
				GameEngine.backgroundPaintObjects.add((IPaintable)obj);
			}
		}
		if(obj instanceof ICollidable){
			if(!GameEngine.collidableObjects.contains(obj)){
				GameEngine.collidableObjects.add((ICollidable)obj);
			}
		}
		if(!(obj instanceof IUpdatable) && !(obj instanceof IPaintable) 
				&& !(obj instanceof ICollidable)){
			throw new ClassCastException(obj + 
					" does not implement IUpdatable, IPaintable or "
					+ "ICollidable");
		}
	}

	/**
	 * Removes the given Object from the GameEngine's internal data 
	 * structure. It will no longer be painted, updated or collided 
	 * with.
	 * @param obj a reference to the object to be removed.
	 * @return true if the object was IPaintable, IUpdatable or 
	 * ICollidable and it was removed successfully.
	 */
	public static boolean remove(Object obj){
		boolean removedFinal = false;
		if(obj instanceof IUpdatable){
			boolean removed = GameEngine.updateObjects.remove((IUpdatable)obj);
			if(removed){
				removedFinal = true;
			}
		}
		if(obj instanceof IPaintable){
			boolean removed = GameEngine.paintObjects.remove(
					(IPaintable)obj);
			if(removed){
				removedFinal = true;
			}
			removed = GameEngine.backgroundPaintObjects.remove(
					(IPaintable)obj);
			if(removed){
				removedFinal = true;
			}
			removed = GameEngine.guiObjects.remove((IPaintable)obj);
			if(removed){
				removedFinal = true;
			}
		}
		if(obj instanceof ICollidable){
			boolean removed = GameEngine.collidableObjects.remove(
					(ICollidable)obj);
			if(removed){
				removedFinal = true;
			}
		}
		return removedFinal;
	}

	/**
	 * Returns an array containing a reference to each unique game 
	 * object. Its length will be the same as the number of unique 
	 * game objects.
	 * @return an array of Objects each implementing IUpdatable, 
	 * IPaintable and/or ICollidable.
	 */
	public static Object[] getGameObjs(){
		HashSet<Object> allObjs = new HashSet<Object>();
		for(int i=0; i<GameEngine.backgroundPaintObjects.size(); i++){
			allObjs.add(GameEngine.backgroundPaintObjects.get(i));
		}
		for(int i=0; i<GameEngine.paintObjects.size(); i++){
			allObjs.add(GameEngine.paintObjects.get(i));
		}
		for(int i=0; i<GameEngine.guiObjects.size(); i++){
			allObjs.add(GameEngine.guiObjects.get(i));
		}	
		for(int i=0; i<GameEngine.updateObjects.size(); i++){
			allObjs.add(GameEngine.updateObjects.get(i));
		}
		for(int i=0; i<GameEngine.collidableObjects.size(); i++){
			allObjs.add(GameEngine.collidableObjects.get(i));
		}
		return allObjs.toArray();
	}

	/**
	 * Returns an array containing a reference to all unique game 
	 * objects that are instances of the given class. The length
	 * of the array will be the same as the number of unique game 
	 * objects.
	 * 
	 * The class path must be fully qualified - it must be preceded
	 * by the package names separated by a dot. For example, if the
	 * classPath is "engine.interfaces.IPaintable", it will return 
	 * all objects implementing IPaintable. However, if the classPath
	 * is just "IPaintable", a ClassNotFoundException will be thrown.
	 * 
	 * @param classPath the fully qualified path of the class or 
	 * interface.
	 * @return an array of all game objects inheriting or 
	 * implementing the given class / interface.
	 * @throws ClassNotFoundException if the classPath does not match
	 * any class or interface in the current working project.
	 */
	public static Object[] getGameObjs(String classPath) 
			throws ClassNotFoundException{
		HashSet<Object> allObjs = new HashSet<Object>();
		
		Object[] gameObjs = GameEngine.getGameObjs();
		for(int i=0; i<gameObjs.length; i++){
			Object obj = gameObjs[i];
			if(Class.forName(classPath).isAssignableFrom(
					obj.getClass())){
				allObjs.add(obj);
			}
		}
		return allObjs.toArray();
	}

	/**
	 * Returns an array of all IPaintable objects being painted in
	 * the middle ground. There will be no null items.
	 * @return an IPaintable array containing all unique IPaintables
	 * in the GameEngine's middle ground.
	 */
	public static IPaintable[] getPaintableObjs(){
		return GameEngine.paintObjects.toArray(new IPaintable[0]);
	}

	/**
	 * Returns an array of all IPaintable objects being painted in
	 * the background. There will be no null items.
	 * @return an IPaintable array containing all unique IPaintables
	 * in the GameEngine's background.
	 */
	public static IPaintable[] getBackgroundPaintableObjs(){
		return GameEngine.backgroundPaintObjects.toArray(new IPaintable[0]);
	}

	/**
	 * Returns an array of all IPaintable objects being painted in
	 * the GUI layer, or foreground. There will be no null items.
	 * @return an IPaintable array containing all unique IPaintables
	 * in the GameEngine's GUI layer.
	 */
	public static IPaintable[] getGUIObjs(){
		return GameEngine.guiObjects.toArray(new IPaintable[0]);
	}

	/**
	 * Returns an array of all ICollidabe objects in the GameEngine.
	 * There will be no null items.
	 * @return an ICollidable array containing all unique 
	 * ICollidables in the GameEngine.
	 */
	public static ICollidable[] getCollidableObjs(){
		return GameEngine.collidableObjects.toArray(new ICollidable[0]);
	}

	/**
	 * Returns an array of all IUpdatable objects in the GameEngine.
	 * There will be no null items.
	 * @return an IUpdatable array containing all unique IUpdatables
	 * in the GameEngine.
	 */
	public static IUpdatable[] getUpdatableObjs(){
		return GameEngine.updateObjects.toArray(new IUpdatable[0]);
	}
	
	/**
	 * Changes the size of the window to the given width and height.
	 * @param width the new window width.
	 * @param height the new window height.
	 */
	public static void setPreferredWindowSize(int width, int height){
		mainWindow.setSize(width, height);
	}

	/**
	 * Maximizes the window so that it fills the screen.
	 */
	public static void maximizeWindow(){
		mainWindow.setExtendedState(JFrame.MAXIMIZED_BOTH);
	}
	
	/**
	 * Gets the MainWindow object which holds the Game's paint
	 * canvas.
	 * @return a reference to the MainWindow object.
	 */
	public static GraphicsWindow getMainWindow(){
		return GameEngine.mainWindow;
	}

	
	/**
	 * Calls the given game's load() method then sets main window 
	 * size to the dimensions returned from game.getWinWidth() and 
	 * game.getWinHeight() and makes it visible. 
	 * It then starts the GameEngine update and paint loop.
	 */
	public static void loadGame(Game g){
		GameEngine.game = g;
		GameEngine.game.load();
		GameEngine.mainWindow.setSize(GameEngine.game.getWinWidth(), 
				GameEngine.game.getWinHeight());
		GameEngine.mainWindow.setVisible(true);
		
		GameEngine.run();
	}
	
	/**
	 * Gets the Game object that has been loaded into the GameEngine.
	 * @return a reference to the Game object, or null if a Game has
	 * not been loaded.
	 */
	public static Game getGame(){
		return GameEngine.game;
	}
	
	/**
	 * Switch debug on if it is off; switch debug off if it is on.
	 */
	public static void toggleDebug(){
		GameEngine.debug(!GameEngine.debug);
	}
	
	/**
	 * Set the GameEngine debugging state to the given boolean.
	 * @param debug true to start debugging.
	 */
	public static void debug(boolean debug){
		GameEngine.debug = debug;

		if(GameEngine.debug){
			GameEngine.mainWindow.showFPS();
		}
		else{
			GameEngine.mainWindow.hideFPS();
		}
	}
	
	/**
	 * Gets the GameEngine's debugging state. 
	 * If this is true, the game should display extra information.
	 * For example, the game could execute:
	 * if(GameEngine.isDebugging()){
	 * 	 System.out.println("Something happened");
	 * }
	 * @return true if the GameEngine is in the debug state.
	 */
	public static boolean isDebugging(){
		return GameEngine.debug;
	}
	
	/**
	 * Set the GameEngine paused state to the given boolean. If this
	 * is true, the GameEngine will not update the Game or IUpdatable
	 * objects and it will not test for collisions between
	 * ICollidable objects.
	 * @param pause true to pause the game.
	 */
	public static void pause(boolean pause){
		GameEngine.paused = pause;
	}
	
	/**
	 * Switch paused on if it is off; switch puased off if it is on.
	 */
	public static void togglePaused(){
		GameEngine.pause(!GameEngine.paused);
	}
	
	/**
	 * Gets the GameEngine's paused state.
	 * If this is true, the game objects will not move and their
	 * update and collision methods will not be executed.
	 * @return true if the GameEngine is in the paused state.
	 */
	public static boolean isPaused(){
		return GameEngine.paused;
	}
}
