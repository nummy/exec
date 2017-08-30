package engine.graphics;

import java.awt.Graphics;

import javax.swing.JPanel;

import engine.GameEngine;
import engine.interfaces.IPaintable;

/**
 * This is where all game objects will be drawn.
 * This panel is automatically constructed by the MainWindow.
 * @author Michael
 *
 */
public class GraphicsPanel extends JPanel{

	/**
	 * Constructs a graphics panel to draw images to.
	 * This object automatically draws all objects added to the GameEngine.
	 */
	public GraphicsPanel(){
		super();
	}

	/**
	 * Do not call this method directly.
	 * Call repaint and it will call this method as a side effect.
	 * This is automatically called by MainWindow.repaint() in the GameEngine.
	 */
	@Override
	public void paintComponent(Graphics g){
		super.paintComponent(g);
		
		IPaintable[] paintObjs = GameEngine.getBackgroundPaintableObjs();
		for(int i=0; i < paintObjs.length; i++){
			IPaintable backgroundObj = paintObjs[i];
			backgroundObj.paint(g);
		}

		paintObjs = GameEngine.getPaintableObjs();
		for(int i=0; i<paintObjs.length; i++){
			IPaintable obj = paintObjs[i];
			obj.paint(g);
		}
		
		paintObjs = GameEngine.getGUIObjs();
		for(int i=0; i<paintObjs.length; i++){
			IPaintable obj = paintObjs[i];
			obj.paint(g);
		}
	}
}
