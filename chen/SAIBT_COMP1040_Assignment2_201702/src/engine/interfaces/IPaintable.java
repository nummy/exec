package engine.interfaces;

import java.awt.Graphics;

/**
 * The IPaintable interface provides methods to allow an object
 * to paint itself to the screen using the javax.swing graphics library.
 * 
 * The engine.graphics.MainWindow class will automatically paint all 
 * IPaintable objects that have been added to the GameEngine. If your 
 * class implements this interface you can add it to the GameEngine.
 * 
 * @author Michael
 * 
 */
public interface IPaintable {

	/**
	 * This method should use the argument Graphics context to draw images
	 * to the screen.
	 * @param g a graphics context for drawing images, text and primitive 
	 * shapes to a javax.swing component.
	 */
	public void paint(Graphics g);
	
}
