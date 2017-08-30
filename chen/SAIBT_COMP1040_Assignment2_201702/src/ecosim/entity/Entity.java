package ecosim.entity;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;

import ecosim.world.Tile;
import engine.GameEngine;
import engine.graphics.Debugger;
import engine.interfaces.IPaintable;
import engine.interfaces.IUpdatable;
import engine.math.BoundingBox;
import engine.math.Vector2D;

/**
 * The Entity class implements the methods from both IUpdatable and
 * IPaintable. It contains a BufferedImage which will be painted to 
 * the window in the paint method. It contains a BoundingBox, which
 * determines the image's position and size. 
 * 
 * The Entity has an abstract update method which will need to be 
 * defined in any descendant classes. If this object is added to the
 * GameEngine using GameEngine.add(obj), its paint method and 
 * update method will be called automatically 60 times per second.
 * 
 * The Animal class in your EcoSim should extend from this class so
 * that any of its descendants can also be drawn to the screen
 * automatically.
 * 
 * @author Michael
 *
 */
public abstract class Entity implements IUpdatable, IPaintable{
	/**
	 * Will be painted in the paint method.
	 */
	protected BufferedImage image;

	/**
	 * Determines the position and size of the image that is painted
	 * in the paint method.
	 */
	protected BoundingBox bounds;

	/**
	 * The location for this object to move its bounds towards. This
	 * should be handled in an overridden update method. This object
	 * can be null. All methods should check for a null target before
	 * accessing its methods or variables.
	 */
	protected Vector2D target;

	/**
	 * Whether this entity can act. If an Entity is not alive, its
	 * update method should not execute and it should be removed from
	 * the GameEngine.
	 */
	private boolean alive;

	/**
	 * Constructs an Entity at the given x and y position. The given
	 * image will determine what is painted to the screen in the
	 * paint method. The Entity and image will have the default size,
	 * which is equal to Tile.WIDTH and Tile.HEIGHT.
	 * @param x the x coordinate of this Entity's top left corner.
	 * @param y the y coordinate of this Entity's top left corner.
	 * @param image the image to display at that location.
	 */
	public Entity(float x, float y, BufferedImage image){
		this.image = image;
		this.bounds = new BoundingBox(x, y, Tile.WIDTH, Tile.HEIGHT);
		this.alive = true;
	}

	/**
	 * Gets the x coordinate of the top left point of the bounds.
	 * @return the x coordinate.
	 */
	public float getX(){
		return this.bounds.getX1();
	}

	/**
	 * Gets the y coordinate of the top left point of the bounds.
	 * @return the y coordinate.
	 */
	public float getY(){
		return this.bounds.getY1();
	}

	/**
	 * Gets a reference to this object's BoundingBox.
	 * @return a reference to this object's BoundingBox.
	 */
	public BoundingBox getBounds(){
		return this.bounds;
	}

	/**
	 * Gets a deep copy of the top left corner of this object's
	 * BoundingBox. You can also get a reference to the position
	 * using this.getBounds().getPosition().
	 * @return a copy of this object's BoundingBox's top left 
	 * position.
	 */
	public Vector2D getPosition(){
		return this.bounds.getPosition().clone();
	}

	/**
	 * Sets the target coordinates of this Entity. This object should
	 * move its position towards its target in the Entity's update
	 * method. setTarget() stores a reference to the given Vector2D 
	 * which means if that Vector2D's x and y coordinates are 
	 * updated or changed, this Entity will have access to the
	 * updated coordinates.
	 * @param target the Vector2D for this object to move towards.
	 */
	public void setTarget(Vector2D target){
		this.target = target;
	}

	/**
	 * Gets a deep copy of the target Vector2D.
	 * @return a copy of the target.
	 */
	public Vector2D getTarget(){
		return this.target.clone();
	}

	/**
	 * Returns whether this Entity is alive and able to act.
	 * @return true if the object should be updating.
	 */
	public boolean isAlive(){
		return this.alive;
	}

	/**
	 * Sets alive to false and removes this object from the
	 * GameEngine. This cannot be undone.
	 */
	public void die(){
		this.alive = false;
		GameEngine.remove(this);
	}

	/**
	 * Paints the object's image to the MainWindow at the location
	 * of this object's bounds, with the same size as this
	 * object's bounds.
	 * 
	 * If this object is added to the GameEngine, this method will
	 * automatically be called 60 times per second.
	 */
	@Override
	public void paint(Graphics g) {
		g.drawImage(image, (int)bounds.getX1(), (int)bounds.getY1(), 
				(int)bounds.getWidth(), (int)bounds.getHeight(), null);
		if(GameEngine.isDebugging()){
			Debugger.drawBounds(g, this.getBounds(), Color.CYAN);
			if(target != null){
				Debugger.drawMovementVector(g, this.getBounds(),
						this.target, Color.BLUE);
			}
		}
	}


}
