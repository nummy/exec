package engine;


/**

 * Your Game object should override loadKeyFunctions(), loadMouseFunctions(),
 * loadImages() and the update() methods. 
 * 
 * The GameEngine requires that a Game object be loaded before the GameEngine
 * can begin execution.
 * @author Michael
 *
 */
public abstract class Game {
	
	/**
	 * Load will call loadKeyFunctions(), loadMouseFunctions and loadImages().
	 * Any class overriding this method should call super.load() and perform
	 * any additional initialization afterwards. 
	 */
	public void load(){
		this.loadImages();
		this.loadKeyFunctions();
		this.loadMouseFunctions();
	}
	
	/**
	 * This method should create the Game's Keyboard Functions and bind them
	 * to appropriate Key Constants in the Keyboard class.
	 */
	protected abstract void loadKeyFunctions();
	
	/**
	 * This method should create the Game's Mouse Functions and bind them 
	 * to appropriate buttons in the Mouse class.
	 */
	protected abstract void loadMouseFunctions();
	
	/**
	 * This method should load the Game's image files and store them in the
	 * ImageLibrary class.
	 */
	protected abstract void loadImages();
	
	/**
	 * This method should return the intended window width in pixels.
	 * This could also serve as the boundary of the Game. You may want
	 * to store the width as an instance variable.
	 * @return the pixel width of the Game.
	 */
	public abstract int getWinWidth();
	
	/**
	 * This method should return the intended window height in pixels.
	 * This could also serve as the boundary of the Game. You may want 
	 * to store the height as an instance variable.
	 * @return the pixel height of the Game.
	 */
	public abstract int getWinHeight();
	
	
	/**
	 * Updates the state of the Game.
	 * Any code that should be called 60 times a second should be added
	 * to this method. 
	 * 
	 * The argument millisElapsed is the number of milliseconds that has
	 * passed since the last call to update(). You can use this to
	 * execute actions based on time rather than frames per second.
	 * 
	 * @param millisElapsed the milliseconds that have passed since the 
	 * last call to this method.
	 */
	public abstract void update(long millisElapsed);
}
