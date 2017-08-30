package ecosim.world;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;

import engine.GameEngine;
import engine.graphics.Debugger;
import engine.interfaces.IPaintable;
import engine.math.BoundingBox;

/**
 * Tile is a background image to be put into a grid of other tiles.
 * A Tile has a rectangle bounds with x and y coordinates and width
 * and height. It draws a rectangular image within this bounds.
 * 
 * @author Michael
 *
 */
public abstract class Tile implements IPaintable {
	
	/**
	 * The default width of a Tile. All objects in the Game are 
	 * scaled to this width.
	 */
	public static final int WIDTH = 96;
	
	/**
	 * The default height of a Tile. All objects in the Game are
	 * scaled to this height.
	 */
	public static final int HEIGHT = 96;
	
	private BufferedImage image;
	private BoundingBox bounds;
	
	/**
	 * Constructs a Tile object at the given x and y coordinates.
	 * The Tile will have the default width and height.
	 * @param x the top left x coordinate
	 * @param y the top left y coordinate
	 * @param img the image to draw at this location. This image will
	 * be scaled to the default width and height.
	 */
	public Tile(float x, float y, BufferedImage img){
		this.image = img;
		this.bounds = new BoundingBox(x, y, Tile.WIDTH, Tile.HEIGHT);
	}
	
	@Override
	public void paint(Graphics g) {
		g.drawImage(image, (int)this.getX(), (int)this.getY(), 
				(int)bounds.getWidth(), (int)bounds.getHeight(), null);
		
		if(GameEngine.isDebugging()){
			Debugger.drawBounds(g, this.getBounds(), Color.GRAY);
		}
	}
	/**
	 * Gets the top left x coordinate of the bounding box.
	 * @return the x coordinate.
	 */
	public float getX(){
		return this.bounds.getX1();
	}
	
	/**
	 * Gets the top left y coordinate of the boundingbox.
	 * @return the y coordinate.
	 */
	public float getY(){
		return this.bounds.getY1();
	}
	
	/**
	 * Gets the BoundingBox that represents this object's boundary.
	 * @return a reference to this object's BoundingBox.
	 */
	public BoundingBox getBounds(){
		return this.bounds;
	}
	
}
