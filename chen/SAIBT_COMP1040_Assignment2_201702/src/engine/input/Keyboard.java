package engine.input;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.HashMap;

import engine.GameEngine;


/**
 * The singleton Keyboard manages key press events and allows you to map a KeyFunction to each Key.
 * If the update method is called in a loop the update method for each KeyFunction will
 * also be called so that any repeatable KeyFunctions are automatically executed if their
 * associated Key is held down.
 * 
 * @author Michael
 */
public class Keyboard implements KeyListener{

	private static HashMap<Integer, Function> 
						keyFunctions = new HashMap<Integer, Function>();

	public static final int LEFT_SHIFT = 1000;
	public static final int LEFT_CTRL = 1001;
	public static final int LEFT_ALT = 1002;
	public static final int RIGHT_SHIFT = 1003;
	public static final int RIGHT_CTRL = 1004;
	public static final int RIGHT_ALT = 1005;

	/**
	 * This singleton Keyboard object can be accessed from anywhere.
	 */
	public static final Keyboard instance = new Keyboard();	
	static{
		Keyboard.loadStandardKeyFunctions();
	}
	
	private Keyboard(){ }


	private static void loadStandardKeyFunctions(){	
		for(int i=0;i<16; i++){					// KeyEvent.VK_Constants before shift, ctrl, alt
			Keyboard.keyFunctions.put(i, new Function(){
				@Override
				public void execute() { }
			});		
		}
		
		for(int i=1000;i<1006; i++){			// Keyboard Constants SHIFT, CTRL, ALT
			Keyboard.keyFunctions.put(i, new Function(){
				@Override
				public void execute() { }
			});		
		}

		for(int i=19;i<526; i++){				// KeyEvent.VK_Constants after shift, ctrl, alt
			Keyboard.keyFunctions.put(i, new Function(){
				@Override
				public void execute() { }
			});		
		}
	}

	/**
	 *
	 * Maps the argument KeyFunction to the key matching the argument key code.
	 * You may map your functions to either KeyEvent VK constants or Keyboard constants.
	 * For Example:
	 * 	Keyboard.setKeyFunction(KeyEvent.VK_SPACE, new KeyFunction(){
	 * 		public void execute(){
	 * 			System.out.println("SPACE");
	 * 		}
	 * 	});
	 * Or:
	 * 	Keyboard.setKeyFunction(Keyboard.LEFT_SHIFT, new KeyFunction(){
	 * 		public void execute(){
	 * 			System.out.println("SHIFT");
	 * 		}
	 * 	});
	 * @param keyCode Must match either a KeyEvent VK constant or Keyboard constant.
	 * @param function An object implementing the KeyFunction abstract methods. Its execute method
	 * will be invoked when the mapped key is pressed.
	 * @return The KeyFunction currently mapped to the argument key code.
	 * @throws KeyCodeException If key code does not match a predefined KeyEvent VK constant or Keyboard constant
	 */
	public static Function setKeyFunction(int keyCode, Function function) throws KeyCodeException {
		if(keyCode == Keyboard.LEFT_ALT || keyCode == Keyboard.LEFT_SHIFT || keyCode == Keyboard.LEFT_CTRL ||
				keyCode == Keyboard.RIGHT_ALT || keyCode == Keyboard.RIGHT_SHIFT || keyCode == Keyboard.RIGHT_CTRL){
			return keyFunctions.put(keyCode, function);
		}
		else if(KeyEvent.getExtendedKeyCodeForChar(keyCode) != KeyEvent.VK_UNDEFINED){
			return keyFunctions.put(keyCode, function);
		}
		throw new KeyCodeException(keyCode);
	}

	/**
	 * Updates the timers on all mapped KeyFunctions so that any repeatable KeyFunctions
	 * will be executed if their key has been held down for the specified delay. 
	 * This method is automatically called by the GameEngine.
	 * @param millisElapsed Milliseconds since last update.
	 */
	public void update(long millisElapsed) {
		// There's a bug in left_alt event
		// System.out.println(Keyboard.keyFunctions.get(Keyboard.LEFT_ALT).getTimer()); 
		
		for(Function f : Keyboard.keyFunctions.values()){
			if(f!=null){
				f.update(millisElapsed);
			}
		}
	}
	
	/**
	 * Accesses the function associated with the argument constant.
	 * Returns true if that key is held down.
	 * @param keyCode A KeyEvent VK Constant or a Keyboard Constant.
	 * @return true if the key exists and is held down, false otherwise.
	 */
	public static boolean isPressed(int keyCode){
		Function func = keyFunctions.get(keyCode);
		if(func != null){
			return func.isPressed();
		}
		else{
			return false;
		}
	}



	@Override
	public void keyPressed(KeyEvent e) {
		if(GameEngine.isDebugging()){
			System.out.println("Pressed: " + KeyEvent.getKeyText(e.getKeyCode()) + " - " + e.getKeyCode());
		}

		Function func = null;
		switch(e.getKeyCode()){
		case KeyEvent.VK_SHIFT:
			if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT){
				func = Keyboard.keyFunctions.get(Keyboard.LEFT_SHIFT);
			}else if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT){
				func = Keyboard.keyFunctions.get(Keyboard.RIGHT_SHIFT);
			}
			break;
		case KeyEvent.VK_CONTROL:
			if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT){
				func = Keyboard.keyFunctions.get(Keyboard.LEFT_CTRL);
			}else if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT){
				func = Keyboard.keyFunctions.get(Keyboard.RIGHT_CTRL);
			}
			break;
		case KeyEvent.VK_ALT:
			if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT){
				func = Keyboard.keyFunctions.get(Keyboard.LEFT_ALT);
			}else if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT){
				func = Keyboard.keyFunctions.get(Keyboard.RIGHT_ALT);
			}
			break;
		default:
			func = Keyboard.keyFunctions.get((int)e.getKeyCode());
		}
		if(func != null){
			if(!func.isPressed()){
				func.press();
			}
		}
	}

	@Override
	public void keyReleased(KeyEvent e) { 
		if(GameEngine.isDebugging()){
			System.out.println("Released: " + KeyEvent.getKeyText(e.getKeyCode()) + " - " + e.getKeyCode());
		}

		Function func = null;
		switch(e.getKeyCode()){
		case KeyEvent.VK_SHIFT:
			if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT){
				func = Keyboard.keyFunctions.get(Keyboard.LEFT_SHIFT);
			}else if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT){
				func = Keyboard.keyFunctions.get(Keyboard.RIGHT_SHIFT);
			}
			break;
		case KeyEvent.VK_CONTROL:
			if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT){
				func = Keyboard.keyFunctions.get(Keyboard.LEFT_CTRL);
			}else if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT){
				func = Keyboard.keyFunctions.get(Keyboard.RIGHT_CTRL);
			}
			break;
		case KeyEvent.VK_ALT:
			if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT){
				func = Keyboard.keyFunctions.get(Keyboard.LEFT_ALT);
			}else if(e.getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT){
				func = Keyboard.keyFunctions.get(Keyboard.RIGHT_ALT);
			}
			break;
		default:
			func = Keyboard.keyFunctions.get((int)e.getKeyCode());
		}
		if(func != null){
			func.release();
		}
	}

	@Override
	public void keyTyped(KeyEvent e) { 
	}

}
