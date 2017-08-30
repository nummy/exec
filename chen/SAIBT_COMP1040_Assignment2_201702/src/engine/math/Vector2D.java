package engine.math;

/**
 * A Vector2D is an x and y coordinate in 2D space. It can be thought
 * of as a direction with the target pointing towards x and y, and
 * the origin at (0x, 0y). The length of the Vector2D is the distance
 * between (0x, 0y) and the instance variables x, y. Vector2D objects 
 * can be used both as positions and as directions.
 * 
 * @author Michael
 *
 */
public class Vector2D {
	private float x, y;
	
	/**
	 * Constructs a vector at the given coordinates
	 * @param x horizontal coordinate.
	 * @param y vertical coordinate.
	 */
	public Vector2D(float x, float y){
		this.x = x;
		this.y = y;
	}
	
	/**
	 * Constructs a vector at the same coordinates as 
	 * the given Vector2D.
	 * @param pos Vector2D to copy.
	 */
	public Vector2D(Vector2D pos) {
		this.x = pos.getX();
		this.y = pos.getY();
	}

	/**
	 * Get the x coordinate.
	 * @return x coordinate represented by this Vector2D.
	 */
	public float getX(){
		return this.x;
	}
	
	/**
	 * Set the x coordinate.
	 * @param x the x value.
	 */
	public void setX(float x){
		this.x = x;
	}
	
	/**
	 * Get the y coordinate.
	 * @return y coordinate represented by this Vector2D.
	 */
	public float getY(){
		return this.y;
	}
	
	/**
	 * Set the y coordinate.
	 * @param y the y value.
	 */
	public void setY(float y){
		this.y = y;
	}
	
	/**
	 * Set the coordinates of this vector2D.
	 * @param x the x value.
	 * @param y the y value.
	 */
	public void set(float x, float y){
		this.x = x;
		this.y = y;
	}
	
	/**
	 * Set the coordinates to the same coordinates represented by the given Vector2D.
	 * @param v the Vector2D to copy.
	 */
	public void set(Vector2D v){
		this.x = v.getX();
		this.y = v.getY();
	}
	
	/**
	 * Adds the given Vector2D's x and y to this object's x and y.
	 * @param other the Vector2D to add.
	 * @return a reference to this object.
	 */
	public Vector2D add(Vector2D other){
		this.x += other.x;
		this.y += other.y;
		return this;
	}
	

	/**
	 * Adds the given x and y to this object's x and y.
	 * @param x the x value to add.
	 * @param y the y value to add.
	 * @return a reference to this object.
	 */
	public Vector2D add(float x, float y){
		this.x += x;
		this.y += y;
		return this;
	}
	
	/**
	 * Subtracts the given Vector2D's x and y from this object's x and y.
	 * @param other the Vector2D to subtract.
	 * @return a reference to this object.
	 */
	public Vector2D subtract(Vector2D other){
		this.x -= other.x;
		this.y -= other.y;
		return this;
	}
	
	/**
	 * Subtracts the given x and y from this object's x and y.
	 * @param x the x value to subtract.
	 * @param y the y value to subtract.
	 * @return a reference to this object.
	 */
	public Vector2D subtract(float x, float y){
		this.x -= x;
		this.y -= y;
		return this;
	}
	
	/**
	 * Divides this object's x and y by the given scale.
	 * @param scale value to divide by.
	 * @return a reference to this object.
	 */
	public Vector2D div(float scale){
		this.x /= scale;
		this.y /= scale;
		return this;
	}
	
	/**
	 * Scales the calling object by the input scale
	 * @param scale amount to multiply the components by
	 * @return a reference to this object
	 */
	public Vector2D scale(float scale){
		this.x *= scale;
		this.y *= scale;
		return this;
	}
	
	/**
	 * Normalizes this object so that the vector is scaled to a length of 1.
	 * @return a reference to this object
	 */
	public Vector2D normalize(){
		float len = (float)this.length();
		if(len != 0){
			this.x /= len;
			this.y /= len;
		}
		return this;
	}	
	
	/**
	 * Calculates and returns the distance between (0, 0) and this object's (x, y).
	 * @return this vector's length.
	 */
	public double length(){
		return Math.sqrt(this.x*this.x + this.y*this.y);
	}
	
	/**
	 * Calculates and returns the distance between the given 
	 * Vector2D's (x, y) and this object's (x, y).
	 * @param other the vector to get the distance from.
	 * @return the distance between this Vector2D and the argument Vector2D.
	 */
	public double distance(Vector2D other){
		return Math.sqrt((this.x - other.x) * (this.x - other.x) +
							(this.y - other.y) * (this.y - other.y));
	}
	
	/**
	 * Rotates this vector the given degrees around the given 
	 * origin point.
	 * @param origin the point to rotate around.
	 * @param degrees the angle to rotate.
	 */
	public void rotate(Vector2D origin, double degrees) {
		double radians = Math.toRadians(degrees);
		
		this.subtract(origin);
		
		this.set((float)(this.getX()*Math.cos(radians)-this.getY()*Math.sin(radians)),
				(float)(this.getY()*Math.cos(radians)+this.getX()*Math.sin(radians)));
		
	
		this.add(origin);
	}	

	@Override
	public boolean equals(Object other){
		if(other!=null && other.getClass() == this.getClass()){
			Vector2D pOther = (Vector2D)other;
			if(pOther.x == this.x && pOther.y == this.y){
				return true;
			}
		}
		return false;
	}
	
	@Override
	public String toString(){
		return "Vector2D: " + this.x + ", " + this.y;
	}
	
	@Override
	public Vector2D clone(){
		return new Vector2D(this);
	}
	
}
