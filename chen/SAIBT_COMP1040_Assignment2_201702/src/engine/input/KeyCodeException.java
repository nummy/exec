package engine.input;

/**
 * This Exception is thrown if the Keyboard attempts to map a key code that 
 * does not match a KeyEvent VK constant or a Keyboard constant. It extends
 * from RunTimeException which means you are not forced to handle it with try
 * and catch if it is unnecessary.
 * 
 * @author Michael
 */
public class KeyCodeException extends RuntimeException{
	
	private final int keycode;
	
	public KeyCodeException(int keycode){
		super("Invalid Key Code " + keycode);
		this.keycode = keycode;
	}
	
	/**
	 * Returns the keycode that caused the error.
	 * @return The keycode that caused the error.
	 */
	public int getKeyCode(){
		return this.keycode;
	}
}
