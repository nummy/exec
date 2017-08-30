package engine.graphics;

import java.awt.Color;
import java.awt.Graphics;

import engine.math.BoundingBox;
import engine.math.Vector2D;

public class Debugger {
	
	public static void drawBounds(Graphics graphics, BoundingBox bounds, Color colour){
		bounds.paint(graphics, colour);
	}

	public static void drawMovementVector(Graphics graphics, BoundingBox bounds, 
			Vector2D targetLocation, Color colour) {
		Vector2D target = targetLocation.clone().add(
				bounds.getWidth()/2, bounds.getHeight()/2);
		Debugger.drawArrow(graphics, bounds.getCenter(), target, colour);
	}
	
	public static void drawArrow(Graphics g, Vector2D pos, Vector2D target, Color c){
		Color oldColour = g.getColor();
		g.setColor(c);		
		g.drawLine((int)pos.getX(), (int)pos.getY(), 
				(int)target.getX(), (int)target.getY());

		Vector2D point1 = pos.clone().subtract(target).normalize().scale(20).add(target);
		Vector2D point2 = pos.clone().subtract(target).normalize().scale(20).add(target);
		
		point1.rotate(target, 30);
		point2.rotate(target, -30);
		
		g.drawLine((int)target.getX(), (int)target.getY(),
				(int)point1.getX(), (int)point1.getY());
		
		g.drawLine((int)target.getX(), (int)target.getY(),
				(int)point2.getX(), (int)point2.getY());
		
		g.setColor(oldColour);
	}

}
