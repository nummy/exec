package engine.math;

/**
 * This exception can be thrown in any situation where an error 
 * would arise from mathematics. In particular, this exception is
 * thrown from the BoundingBox class if the width and height are 
 * set to negative numbers.
 * 
 * @author Michael
 *
 */
public class MathException extends RuntimeException{
	
	private Object badMaths;
	
	/**
	 * Constructs a MathException instance with a custom error
	 * message. Note the actual error message will be 
	 * message + " " + badMaths. 
	 * @param message a String to decorate the maths.
	 * @param badMaths an object representing the math error that
	 * occurred.
	 */
	public MathException(String message, Object badMaths){
		super(message + " " + badMaths);
		this.badMaths = badMaths;
	}
	
	/**
	 * Constructs a MathException instance with a custom error
	 * message. Note getBadObj() will return null if constructed in 
	 * this way.
	 * @param message a String to represent the math error that 
	 * occurred.
	 */
	public MathException(String message){
		super(message);
	}
	
	/**
	 * Constructs a MathException instance with the default error
	 * message "Mathematically impossible: " + badMaths.
	 * @param badMaths an object representing the math error that
	 * occurred.
	 */
	public MathException(Object badMaths){
		super("Mathematically impossible: " + badMaths);
		this.badMaths = badMaths;
	}
	
	/**
	 * Gets the object representing the math error that occurred. 
	 * This could be an Integer or String or something else.
	 * @return the object representing the math error that occurred.
	 */
	public Object getBadObj(){
		return this.badMaths;
	}
	
}
