package engine.input;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

import engine.GameEngine;
import engine.math.Vector2D;


/**
 * This singleton Mouse does not need to be constructed. 
 * The only available Mouse object can be accessed from MouseInputListener.instance.
 * From this class you may access the Mouse's last position and check if any of the 
 * three standard buttons are pressed.
 * Functions can be bound to each of the three standard buttons by adding an object that 
 * implements KeyFunction to the appropriate button.
 * Only one KeyFunction can be added to each button.
 * 
 * @author Michael
 *
 */
public class Mouse implements MouseListener, MouseMotionListener {

	/**
	 * The MainWindow automatically accesses this to process mouse motion 
	 * and mouse pressed events. You should only have to access the static
	 * methods in this class.
	 */
	public static final Mouse instance = new Mouse();	
	private static Vector2D lastPos = new Vector2D(0, 0);
	
	private static boolean leftPressed = false;
	private static boolean middlePressed = false;
	private static boolean rightPressed = false;
	private static Function leftFunction = null;
	private static Function rightFunction = null;
	private static Function middleFunction = null;
	
	private Mouse(){}
	
	@Override
	public void mouseClicked(MouseEvent e) { }
	@Override
	public void mouseEntered(MouseEvent e) { }
	@Override
	public void mouseExited(MouseEvent e) { }
	
	@Override
	public void mouseDragged(MouseEvent e) { 
		Mouse.lastPos.set(e.getX(), e.getY());
	}
	@Override
	public void mouseMoved(MouseEvent e) { 
		Mouse.lastPos.set(e.getX(), e.getY());
	}

	public static Vector2D getLastPos() {
		return new Vector2D(Mouse.lastPos);
	}

	@Override
	public void mousePressed(MouseEvent e) {
		if(GameEngine.isDebugging()){
			System.out.println("Click @ " + Mouse.lastPos);
		}
		if(e.getButton() == MouseEvent.BUTTON1){
			Mouse.leftPressed = true;
			if(Mouse.leftFunction != null){
				Mouse.leftFunction.press();
			}
		}
		else if(e.getButton() == MouseEvent.BUTTON2){
			Mouse.middlePressed = true;
			if(Mouse.middleFunction != null){
				Mouse.middleFunction.press();
			}
		}
		else if(e.getButton() == MouseEvent.BUTTON3){
			Mouse.rightPressed = true;
			if(Mouse.rightFunction != null){
				Mouse.rightFunction.press();
			}
		}
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		if(e.getButton() == MouseEvent.BUTTON1){
			Mouse.leftPressed = false;
			if(Mouse.leftFunction != null){
				Mouse.leftFunction.release();
			}
		}
		else if(e.getButton() == MouseEvent.BUTTON2){
			Mouse.middlePressed = false;
			if(Mouse.middleFunction != null){
				Mouse.middleFunction.release();
			}
		}
		else if(e.getButton() == MouseEvent.BUTTON3){
			Mouse.rightPressed = false;
			if(Mouse.rightFunction != null){
				Mouse.rightFunction.release();
			}
		}
	}

	public void update(long millisElapsed) {
		if(leftFunction!=null){
			leftFunction.update(millisElapsed);
		}
		if(rightFunction!=null){
			rightFunction.update(millisElapsed);
		}
		if(middleFunction!=null){
			middleFunction.update(millisElapsed);
		}
	}
	
	public static boolean isLeftDown(){
		return Mouse.leftPressed;
	}
	
	public static boolean isRightDown(){
		return Mouse.rightPressed;
	}
	
	public static boolean isMiddleDown(){
		return Mouse.middlePressed;
	}
	
	public static Function setMiddleFunction(Function func){
		Function temp = Mouse.middleFunction;
		Mouse.middleFunction = func;
		return temp;
	}
	
	public static Function setLeftFunction(Function func){
		Function temp = Mouse.leftFunction;
		Mouse.leftFunction = func;
		return temp;
	}
	
	public static Function setRightFunction(Function func){
		Function temp = Mouse.rightFunction;
		Mouse.rightFunction = func;
		return temp;
	}
}
