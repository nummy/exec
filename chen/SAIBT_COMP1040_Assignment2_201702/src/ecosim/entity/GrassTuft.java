package ecosim.entity;

import java.awt.Color;
import java.awt.Graphics;

import engine.GameEngine;
import engine.graphics.Debugger;
import engine.graphics.ImageLibrary;

/**
 * A GrassTuft is an edible Grass entity. Wombats will move towards
 * GrassTuft objects and eat them if they are hungry. GrassTufts will
 * only grow on GrassTile objects in a place that is not already
 * taken by another GrassTuft. The EcoSim update method should add a
 * GrassTuft on a random GrassTile that is not already taken every
 * 1000 milliseconds.
 * @author Michael
 *
 */
public class GrassTuft extends Entity{
	
	/**
	 * Constructs a Grass tuft at the given x and y location.
	 * It will have the default image. Wombats will try to eat this.
	 * @param x the x coordinate of this object's bounds.
	 * @param y the y coordinate of this object's bounds.
	 */
	public GrassTuft(float x, float y){
		super(x, y, ImageLibrary.get("grass_tuft"));
	}
	
	/**
	 * The update method for GrassTufts does nothing. Maybe it would
	 * be more efficient if this was not an IUpdatable object.
	 */
	@Override
	public void update(long millisElapsed) { }
	
	@Override
	public void paint(Graphics g) {
		g.drawImage(image, (int)bounds.getX1(), (int)bounds.getY1(), (int)bounds.getWidth(), (int)bounds.getHeight(), null);
		if(GameEngine.isDebugging()){
			Debugger.drawBounds(g, this.getBounds().clone().scale(0.995f), Color.WHITE);
		}
	}
}
