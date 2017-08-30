package engine.interfaces;

import engine.math.BoundingBox;

/**
 * The ICollidable interface provides methods for checking if this
 * object has collided with another object. To do this, you will need
 * to check that this object's bounds intersects with the other 
 * object's bounds.
 * 
 * If your class implements the ICollidable interface, it can be added 
 * to the GameEngine. If an ICollidable object has been added to the 
 * GameEngine, it will call collidedWith between your object and all
 * other ICollidable objects in the GameEngine. If any have collided,
 * it will call onCollision to process the collision event.
 * 
 * @author Michael
 */
public interface ICollidable {
	
	/**
	 * This should return the BoundingBox that serves as this object's
	 * boundary. getBounds() allows other ICollidables to access this object's
	 * BoundingBox so that they can check if their BoundingBox has collided 
	 * with it. To optimize memory management, your object should store the
	 * BoundingBox as an instance variable.
	 * @return this object's BoundingBox
	 */
	public BoundingBox getBounds();
	
	
	/**
	 * Returns true if this object's BoundingBox has intersected the other object's
	 * BoundingBox. For Example, a reasonable way to implement this method might be:
	 * public boolean collided(ICollidable other){
	 * 	return this.getBounds().intersects(other.getBounds());
	 * }
	 * More complexity could be added for pixel collision detection but keep in mind, 
	 * if this.collided(that) returns true then that.collided(this) should also 
	 * return true.
	 * 
	 * @param other the ICollidable to check against this bounds.
	 * @return true if this bounds has collided with the other bounds.
	 */
	public boolean collidedWith(ICollidable other);
	
	/**
	 * If this ICollidable has been added to the GameEngine then the GameEngine will
	 * automatically check if this object has collided with any other ICollidable.
	 * If a collision is detected, the GameEngine will call this method on the object
	 * that returned true from their collided(other) method.
	 * @param other the object that collided with this.
	 */
	public void onCollision(ICollidable other);
	
}
