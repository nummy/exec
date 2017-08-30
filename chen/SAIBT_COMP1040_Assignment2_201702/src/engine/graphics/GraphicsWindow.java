package engine.graphics;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JLabel;

import engine.input.Mouse;
import engine.math.Vector2D;

/**
 * The window that contains the panel that draws the contents of the game engine.
 * 
 * @author Michael
 */
public class GraphicsWindow extends JFrame{

	private final GraphicsPanel canvas;
	private JLabel fpsDisplay;
	private long lastTime;
	private long refreshTimer;
	
	/**
	 * Initializes a canvas for drawing BufferedImages to.
	 */
	public GraphicsWindow(){
		super();
		this.canvas = new GraphicsPanel();
		this.canvas.setFocusable(true);
		this.fpsDisplay = new JLabel("0 fps");
		this.fpsDisplay.setForeground(Color.WHITE);
		this.canvas.add(fpsDisplay).setVisible(false);
		this.add(canvas, BorderLayout.CENTER);
	}

	@Override
	public void setSize(Dimension size){
		this.canvas.setPreferredSize(size);
		super.pack();
	}

	@Override
	public void setSize(int width, int height){
		this.canvas.setPreferredSize(new Dimension(width, height));
		super.pack();
	}

	@Override
	public void setBackground(Color c){
		super.setBackground(c);
		if(this.canvas != null){
			this.canvas.setBackground(c);
		}
	}
	
	/**
	 * Gets the canvas that is used for painting.
	 * @return a reference to this object's GraphicsPanel.
	 */
	public GraphicsPanel getCanvas(){
		return this.canvas;
	}

	/**
	 * Gets the center of the canvas
	 * @return Center position relative to top left of window.
	 */
	public Vector2D getCanvasCenter(){
		System.out.println(canvas.getWidth() + ", " + canvas.getHeight());
		return new Vector2D(canvas.getWidth()/2, canvas.getHeight()/2);
	}
	
	/**
	 * A KeyListener must be added to the canvas so that it accepts keyboard events.
	 * @param listener An object that implements KeyListener
	 */
	public void addKeyboard(KeyListener listener){
		this.canvas.addKeyListener(listener);
	}
	
	/**
	 * A Mouse object must be added to the canvas so that it accepts mouse events.
	 * It must be added to the canvas to track the correct mouse position, not the frame.
	 * Call this method, not addMouseListener or addMouseMotionListener.
	 * @param mouse An object that implements MouseListener and MouseMotionListener
	 */
	public void addMouse(Mouse mouse){
		this.canvas.addMouseListener(mouse);
		this.canvas.addMouseMotionListener(mouse);
	}
	
	/**
	 * Displays an FPS counter as a JLabel.
	 */
	public void showFPS(){
		this.fpsDisplay.setVisible(true);
	}

	/**
	 * Hides the FPS counter JLabel.
	 */
	public void hideFPS(){
		this.fpsDisplay.setVisible(false);
	}
	
	/**
	 * Updates the FPS counter every second.
	 * This is automatically called by the GameEngine.
	 * @param millisElapsed
	 */
	public void update(long millisElapsed) {
		refreshTimer += millisElapsed;
		if(fpsDisplay.isVisible() && refreshTimer > 1000){
			double fps = 1000000000.0 / (System.nanoTime() - this.lastTime);
			fpsDisplay.setText(String.format("%.2f", fps) + " fps");
			refreshTimer = refreshTimer % 1000;
		}
		this.lastTime = System.nanoTime();
	}
}
