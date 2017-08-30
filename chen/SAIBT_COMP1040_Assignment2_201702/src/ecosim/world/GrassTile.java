package ecosim.world;

import engine.graphics.ImageLibrary;

/**
 * A GrassTile is simply a green tile. They are special because they
 * are the only tiles that can spawn a GrassTuft on them.
 * 
 * @author Michael
 *
 */
public class GrassTile extends Tile{
	
	/**
	 * Constructs a GrassTile with its top left point at the given
	 * x and y.
	 * @param x the top left x coordinate.
	 * @param y the top left y coordinate.
	 */
	public GrassTile(float x, float y) {
		super(x, y, ImageLibrary.get("grass_tile"));
	}

}
