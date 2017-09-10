package ecosim.exception;
/**  
/ File: fileName.java 
/ Author: your name  
/ Id: your id  
/ Version: 1.0 today¡¯s date  
/ Description: Assignment 2 - ¡­.  
/ This is my own work as defined by the SAIBT 
/ Academic Misconduct policy.  
*/  
import engine.math.Vector2D;
public class OutOfBoundsException extends Exception{
	private Vector2D badPosition;
	/**
	 * constructor for the OutOfTheBoundsException
	 * @param position
	 */
	public OutOfBoundsException(Vector2D position) {
		super("Out of bounds:" + position.toString());
		badPosition = position;
	}
	/**
	 * get the BadPosition
	 * @return
	 */
	public Vector2D getBadPosition() {
		return badPosition;
	}
}
