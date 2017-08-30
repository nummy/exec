package engine.math;

import java.awt.Color;
import java.awt.Graphics;

import engine.GameEngine;

/**
 * 
 * The BoundingBox represents a rectangle in 2D space.
 * It contains a position, width and height and various methods for
 * moving and resizing the box, as well as some methods for checking 
 * if two BoundingBoxes have collided.
 * 
 * @author Michael
 *
 */
public class BoundingBox {

	/**
	 * Side is usually used to indicate which side of a BoundingBox object
	 * has collided with another BoundingBox.
	 * @author mul
	 *
	 */
	public enum Side {
		LEFT, TOP, RIGHT, BOTTOM;
	}

	private Vector2D position;
	private float width, height;

	/**
	 * Constructs a BoundingBox by specifying the topleft coordinates 
	 * and the width and height.
	 * @param leftX	the x coordinate of the left side of the box.
	 * @param topY the y coordinate of the top side of the box.
	 * @param width the distance from left to right.
	 * @param height the distance from top to bottom.
	 * @throws MathException if width or height are negative.
	 */
	public BoundingBox(float leftX, float topY, float width, float height) 
			throws MathException{
		if(width < 0){
			throw new MathException("Impossible width: ", width);
		}
		if(height < 0){
			throw new MathException("Impossible width: ", width);
		}
		this.position = new Vector2D(leftX, topY);
		this.width = width;
		this.height = height;
	}

	/**
	 * Constructs a deep copy of the argument object so that this object
	 * is an independent copy of the original with the same values for x, y,
	 * width and height.
	 * @param other the BoundingBox to copy.
	 */
	public BoundingBox(BoundingBox other){
		this.position = new Vector2D(other.position);
		this.width = other.width;
		this.height = other.height;
	}

	/**
	 * This returns a BoundingBox of the given width and height, centered at the given
	 * Vector2D. This means the top left will be at (center.x-width/2, center.y-height/2).
	 * The bottom right will be at (center.x+width/2, center.height+height/2).
	 * @param center the center coordinates of the new BoundingBox.
	 * @param width the total width of the BoundingBox.
	 * @param height the total height of the BoundingBox.
	 * @return a new BoundingBox with its center coordinates at the given center of the
	 * given width and height.
	 * @throws MathException if width or height are negative.
	 */
	public static BoundingBox getCenteredInstance(Vector2D center, float width, float height)
			throws MathException{
		if(width < 0){		
			throw new MathException("Negative width:", width);
		}
		if(height < 0){		
			throw new MathException("Negative height:", height);
		}
		return new BoundingBox(center.getX() - width / 2, center.getY() - height / 2, width, height);
	}

	/**
	 * Checks if the given point is between this BoundingBox's top left and 
	 * bottom right coordinates.
	 * @param point the Vector2D to check.
	 * @return true if the given point is inside this BoundingBox.
	 */
	public boolean contains(Vector2D point){
		if(point.getX() > this.getX1() && 
				point.getX() < this.getX1() + this.width &&
				point.getY() > this.getY1() && 
				point.getY() < this.getY1() + this.height){
			return true;
		}
		return false;
	}

	/**
	 * Checks to see if the given BoundingBox overlaps with this BoundingBox.
	 * @param other the BoundingBox to compare with this.
	 * @return true if this BoundingBox contains any corner point from the other BoundingBox.
	 */
	public boolean intersects(BoundingBox other){
		if(	other.contains(this.getBottomLeft()) 	||				
				other.contains(this.getBottomRight()) 	||
				other.contains(this.getTopLeft()) 		||
				other.contains(this.getTopRight())) {
			//one or more corners inside other box
			return true;
		}
		else if(this.contains(other.getBottomLeft()) 	|| 		
				this.contains(other.getBottomRight()) 	||
				this.contains(other.getTopLeft()) 		||
				this.contains(other.getTopRight())){
			//other fully contained in other box
			return true;
		}
		return false;
	}

	/**
	 * Finds the area that is overlapping between this object and the given
	 * BoundingBox. This rectangle is returned as a new BoundingBox. If the
	 * BoundingBoxes are not overlapping, it returns null.
	 * @param other the BoundingBox to compare
	 * @return a rectangle representing the intersected area or null if no
	 * intersection was found.
	 */
	public BoundingBox getIntersectedArea(BoundingBox other){
		if(this.intersects(other)){
			BoundingBox area = new BoundingBox(this);

			if(!other.contains(this.getTopLeft()) && !other.contains(this.getBottomLeft()) &&
					!this.contains(other.getTopRight()) && !this.contains(other.getBottomRight())){
				//Left
				try{
					area.setX1(other.getX1(), false);	
				}
				catch(MathException e){
					area.paint(GameEngine.getMainWindow().getCanvas().getGraphics(), Color.CYAN);
					throw e;
				}
			}
			if(!other.contains(this.getTopLeft()) && !other.contains(this.getTopRight()) &&
					!this.contains(other.getBottomLeft()) && !this.contains(other.getBottomRight())){
				//Top
				try{
					area.setY1(other.getY1(), false);
				}
				catch(MathException e){
					area.paint(GameEngine.getMainWindow().getCanvas().getGraphics(), Color.CYAN);
					throw e;
				}
			}
			if(!other.contains(this.getTopRight()) && !other.contains(this.getBottomRight()) &&
					!this.contains(other.getTopLeft()) && !this.contains(other.getBottomLeft())){
				//Right
				try{
					area.setX2(other.getX2(), false);
				}
				catch(MathException e){
					area.paint(GameEngine.getMainWindow().getCanvas().getGraphics(), Color.CYAN);
					throw e;
				}
			}
			if(!other.contains(this.getBottomLeft()) && !other.contains(this.getBottomRight()) &&
					!this.contains(other.getTopLeft()) && !this.contains(other.getTopRight())){
				//Bottom
				try{
					area.setY2(other.getY2(), false);
				}
				catch(MathException e){
					area.paint(GameEngine.getMainWindow().getCanvas().getGraphics(), Color.CYAN);
					throw e;
				}
			}

			return area;
		}
		return null;
	}

	/**
	 * Returns the side of this rectangle that collided with the other box
	 * WARNING - Will fail at high speeds.
	 * @param other the BoundingBox to compare.
	 * @return Side.RIGHT if this object's right side collided with the given BoundingBox;
	 * Side.LEFT if this object's left side collided with the given BoundingBox;
	 * Side.TOP if this object's top side collided with the given BoundingBox;
	 * Side.BOTTOM if this object's bottom side collided with the given BoundingBox.
	 */
	public Side checkCollision(BoundingBox other){
		BoundingBox area = getIntersectedArea(other);
		if(area!=null){	
			if(area.getHeight() > area.getWidth()){
				//Either right or left
				if(this.getX1() < other.getX1()){
					return Side.RIGHT;
				}
				else{
					return Side.LEFT;
				}
			}
			else if(area.getHeight() < area.getWidth()){ 
				//width >= height
				//Either top or bottom
				if(this.getY1() < other.getY1()){
					return Side.BOTTOM;
				}
				else{
					return Side.TOP;
				}
			}
		}
		return null;
	}

	/**
	 * Gets the x coordinate of the top left corner of this BoundingBox.
	 * @return the x coordinate of the top left corner.
	 */
	public float getX1(){
		return this.position.getX();
	}

	/**
	 * Changes the x coordinate of the top left corner of this BoundingBox.
	 * @param x the new x coordinate of the top left.
	 * @param maintainSize if this is true, the bottom right corner will
	 * move relative to the top left corner. If this is false, the bottom 
	 * right corner will stay in its current position relative to the global 
	 * origin.
	 * @throws MathException if maintainSize is false and the resulting BoundingBox 
	 * would have a negative width.
	 */
	public void setX1(float x, boolean maintainSize) throws MathException{
		if(!maintainSize){
			if(this.width - (x - this.getX1()) < 0){
				throw new MathException("Negative width:", this.width - (x - this.getX1()));
			}
			this.width -= x - this.getX1();
		}
		this.position.setX(x);
	}

	/**
	 * Gets the y coordinate of the top left corner of this BoundingBox.
	 * @return the y coordinate of the top left corner.
	 */
	public float getY1(){
		return this.position.getY();
	}

	/**
	 * Changes the y coordinate of the top left corner of this BoundingBox.
	 * @param y the new y coordinate of the top left.
	 * @param maintainSize if this is true, the bottom right corner will
	 * move relative to the top left corner. If this is false, the bottom 
	 * right corner will stay in its current position relative to the global 
	 * origin.
	 * @throws MathException if maintainSize is false and the resulting BoundingBox 
	 * would have a negative height.
	 */
	public void setY1(float y, boolean maintainSize) throws MathException{
		if(!maintainSize){
			if(this.height - (y - this.getY1()) < 0){
				throw new MathException("Negative height:", this.height - (y - this.getY1()));
			}
			this.height -= y - this.getY1();
		}
		this.position.setY(y);
	}


	/**
	 * Changes the x coordinate of the bottom right corner of this BoundingBox.
	 * @param x the new x coordinate of the bottom right.
	 * @param maintainSize if this is true, the top left corner will
	 * move relative to the bottom right corner. If this is false, the top 
	 * left corner will stay in its current position relative to the global 
	 * origin.
	 */
	public float getX2(){
		return this.getX1() + this.getWidth();
	}

	/**
	 * Changes the x coordinate of the bottom right corner of this BoundingBox.
	 * @param x the new x coordinate of the bottom right.
	 * @param maintainSize if this is true, the top left corner will
	 * move relative to the bottom right corner. If this is false, the top 
	 * left corner will stay in its current position relative to the global 
	 * origin.
	 * @throws MathException if maintainSize is false and the resulting BoundingBox 
	 * would have a negative width.
	 */
	public void setX2(float x, boolean maintainSize) throws MathException{
		if(!maintainSize){
			if(x - this.getX1() < 0){
				throw new MathException("Negative width:", x - this.getX1());
			}
			this.width = x - this.getX1();
		}
		else{
			this.position.setX(this.position.getX() + (x - this.getX2()));
		}
	}

	/**
	 * Gets the y coordinate of the bottom right corner of this BoundingBox.
	 * @return the y coordinate of the bottom right corner.
	 */
	public float getY2(){
		return this.getY1() + this.getHeight();
	}

	/**
	 * Changes the y coordinate of the bottom right corner of this BoundingBox.
	 * @param y the new y coordinate of the bottom right.
	 * @param maintainSize if this is true, the top left corner will
	 * move relative to the bottom right corner. If this is false, the top 
	 * left corner will stay in its current position relative to the global 
	 * origin.
	 * @throws MathException if maintainSize is false and the resulting BoundingBox 
	 * would have a negative height.
	 */
	public void setY2(float y, boolean maintainSize) throws MathException{
		if(!maintainSize){
			if(y - this.getY1() < 0){
				throw new MathException("Negative height:", y - this.getY1());
			}
			this.height = y - this.getY1();
		}
		else{
			this.position.setY(this.position.getY() + (y - this.getY2()));
		}
	}

	/**
	 * Returns the total width of the BoundingBox.
	 * @return the total width.
	 */
	public float getWidth(){
		return this.width;
	}

	/**
	 * Returns the total height of the BoundingBox.
	 * @return the total height.
	 */
	public float getHeight(){
		return this.height;
	}

	/**
	 * Changes the total height of the BoundingBox. 
	 * The bottom right corner will move; its y coordinate becoming 
	 * topLeft.y + newHeight.
	 * @param newHeight the new total height of the BoundingBox.
	 * @throws MathException if newHeight is negative.
	 */
	public void setHeight(float newHeight) throws MathException{
		if(newHeight < 0){
			throw new MathException("Negative height:", newHeight);
		}
		this.height = newHeight;
	}

	/**
	 * Changes the total height of the BoundingBox. 
	 * Both the bottom right corner and top left corner will move;
	 * expanding and shrinking relative to the center of the 
	 * Bounding Box.
	 * @param newHeight the new total height of the BoundingBox.
	 * @throws MathException if the newHeight would be negative.
	 */
	public void setHeightCentered(float newHeight) throws MathException{
		if(newHeight < 0){
			throw new MathException("Negative height:", newHeight);
		}
		float difference = this.height - newHeight;
		setY1(this.getY1() + difference/2, false);
		setY2(this.getY2() - difference/2, false);
	}

	/**
	 * Changes the total width of the BoundingBox. 
	 * The bottom right corner will move; its x coordinate becoming 
	 * topLeft.x + newWidth.
	 * @param newWidth the new total height of the BoundingBox.
	 */
	public void setWidth(float newWidth){
		this.width = newWidth;
	}

	/**
	 * Changes the total width of the BoundingBox. 
	 * Both the bottom right corner and top left corner will move;
	 * expanding and shrinking relative to the center of the 
	 * Bounding Box.
	 * @param newWidth the new total width of the BoundingBox.
	 * @throws MathException if the newWidth is negative.
	 */
	public void setWidthCentered(float newWidth) throws MathException{
		if(newWidth < 0){
			throw new MathException("Negative width:", newWidth);
		}
		float difference = this.width - newWidth;
		setX1(this.getX1() + difference/2, false);
		setX2(this.getX2() - difference/2, false);
	}

	/**
	 * Changes the position of the top left point of the BoundingBox.
	 * The bottom right position will move relative to the top left.
	 * @param position the new position of the top left corner.
	 */
	public void setPosition(Vector2D position){
		this.position.set(position);
	}

	/**
	 * Changes the position of the top left point of the BoundingBox.
	 * The bottom right position will move relative to the top left.
	 * @param x the new x coordinate of the top left corner.
	 * @param y the new y coordinate of the top left corner.
	 */
	public void setPosition(float x, float y){
		this.position.set(x, y);
	}

	/**
	 * Returns the top left position as a Vector2D.
	 * @return a deep copy of the top left position of this BoundingBox.
	 */
	public Vector2D getPosition(){
		return this.getTopLeft();
	}
	
	/**
	 *  Returns a reference to the top left position as a Vector2D.
	 *  Warning: this may cause unexpected side effects if this
	 *  reference is changed from multiple objects.
	 * @return a reference to the top left position of this BoundingBox.
	 */
	public Vector2D getPositionReference() {
		return this.position;
	}

	/**
	 * Returns a Vector2D representing the center of this BoundingBox.
	 * This is equal to this.getPosition().add(this.getWidthHeightVec().scale(0.5)).
	 * @return a new Vector2D representing the center position of this
	 * BoundingBox. Note that the origin of the BoundingBox is the top left;
	 * The center of the BoundingBox and the BoundingBox position are not equal.
	 */
	public Vector2D getCenter(){
		return new Vector2D(this.getX1() + this.width / 2, 
				this.getY1() + this.height / 2);
	}

	/**
	 * All points in the BoundingBox will move by the given Vector2D. The
	 * x and y components of the given Vector2D will be added to the position
	 * of this BoundingBox.
	 * @param movement the direction and distance to move the BoundingBox.
	 */
	public void move(Vector2D movement){
		this.position.add(movement);
	}

	/**
	 * All points in the BoundingBox will move by the given x and y.
	 * @param x the amount to add to the x coordinates.
	 * @param y the amount to add to the y coordinates.
	 */
	public void move(float x, float y){
		this.position.add(x, y);
	}

	/**
	 * Returns a new vector2D representing the top left point in the BoundingBox.
	 * Note that this is equal to calling this.getPosition().
	 * @return a deep copy of the top left position of the BoundingBox.
	 */
	public Vector2D getTopLeft(){
		return new Vector2D(this.position);
	}

	/**
	 * Returns a new vector2D representing the top right point in the BoundingBox.
	 * @return a deep copy of the top right position of the BoundingBox.
	 */
	public Vector2D getTopRight(){
		return new Vector2D(this.getX1() + this.width, 
				this.getY1());
	}

	/**
	 * Returns a new vector2D representing the bottom right point in the BoundingBox.
	 * @return a deep copy of the bottom right position of the BoundingBox.
	 */
	public Vector2D getBottomRight(){
		return new Vector2D(this.getX1() + this.width, 
				this.getY1() + this.height);
	}

	/**
	 * Returns a new vector2D representing the bottom left point in the BoundingBox.
	 * @return a deep copy of the bottom left position of the BoundingBox.
	 */
	public Vector2D getBottomLeft(){
		return new Vector2D(this.getX1(), 
				this.getY1() + this.height);
	}

	/**
	 * Returns a new Vector2D representing the width and height of this BoundingBox 
	 * as a single object. Note that this is relative to the BoundingBox's top left.
	 * @return a Vector2D containing the width and height of this BoundingBox.
	 */
	public Vector2D getWidthHeightVec(){
		return new Vector2D(this.getWidth(), this.getHeight());
	}

	/**
	 * Calculates and returns the total area of this BoundingBox.
	 * @return width multiplied by height.
	 */
	public float getArea(){
		return this.width * this.height;
	}
	
	/**
	 * Multiplies the width and height by the given scale.
	 * The BoundingBox is scaled using the center as the origin.
	 * @param scale the value to scale the BoundingBox by.
	 * @return a reference to this BoundingBox.
	 */
	public BoundingBox scale(float scale){
		this.setHeightCentered(this.getHeight()*scale);
		this.setWidthCentered(this.getWidth()*scale);
		return this;
	}	

	/**
	 * Calculates and returns the distance between the position of this BoundingBox
	 * and the position of the given BoundingBox.
	 * @param other the target BoundingBox
	 * @return the distance between this object and the target BoundingBox.
	 */
	public double distance(BoundingBox other){
		return this.getPosition().subtract(other.getPosition()).length();
	}

	/**
	 * Draws the outline of this BoundingBox to the given Graphics context. This can
	 * be used to paint the BoundingBox to a variety of javax.swing components. The outline
	 * will be drawn in the given colour object and will be 1 pixel in width.
	 * @param g the Graphics context to draw the BoundingBox to.
	 * @param colour the colour of the outline.
	 */
	public void paint(Graphics g, Color colour){
		Color c = g.getColor();
		g.setColor(colour);
		g.drawRect((int)getX1(), (int)getY1(), (int)getWidth(), (int)getHeight());
		g.setColor(c);
	}

	@Override
	public String toString(){
		return "BoundingBox: ("+this.getX1() + ", " + this.getY1() + ") - (" + this.getX2() + ", " + this.getY2()+")";
	}
	
	@Override
	public BoundingBox clone(){
		return new BoundingBox(this);
	}

}
