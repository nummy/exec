package engine.interfaces;

/**
 * The IUpdatable interface provides methods for changing the state of
 * the implementing object many times in a second. 
 * 
 * If your class implements the IUpdatable interface, it can be added 
 * to the GameEngine. If an IUpdatable object has been added to the 
 * GameEngine, it will attempt to call the object's update method 60 
 * times per second.
 * 
 * @author Michael
 *
 */
public interface IUpdatable {
	
	/**
	 * Updates the state of the object.
	 * Any code that should be called 60 times a second should be added
	 * to this method. For example, you could update your object's position.
	 * 
	 * The argument millisElapsed is the number of milliseconds that has
	 * passed since the last call to update(). You can use this to scale 
	 * your movement vector.
	 * 
	 * @param millisElapsed the milliseconds that have passed since the 
	 * last call to this method.
	 */
	public void update(long millisElapsed);
	
}
