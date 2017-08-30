package ecosim.world;

import engine.graphics.ImageLibrary;

/**
 * The SandTile is simply a yellow tile. The SandTile cannot grow 
 * GrassTufts on top of it.
 * @author Michael
 *
 */
public class SandTile extends Tile {

	/**
	 * Constructs a SandTile with its top left point at the given
	 * x and y.
	 * @param x the top left x coordinate.
	 * @param y the top left y coordinate.
	 */
	public SandTile(float x, float y) {
		super(x, y, ImageLibrary.get("sand_tile"));
	}

}
