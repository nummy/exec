package ecosim.entity;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;

import engine.GameEngine;
import engine.graphics.Debugger;

public abstract class Animal extends Entity{

	private int timer;
	protected int energy;
	protected int maxBreedTime;
	protected int breedTime;
	protected float speed;

	public Animal(float x, float y, BufferedImage image, 
			int energy, int breedSteps, float moveSpeed) {
		super(x, y, image);
		
	}

	public abstract Animal breed();
	
	public abstract void selectTarget();
	
	@Override
	public void update(long millisElapsed) {
		
	}
	
	@Override
	public void paint(Graphics g) {
		super.paint(g);
		if(GameEngine.isDebugging()){
			float red = Math.max(1 - this.energy / 10f, 0.0f);
			float blue = Math.min(this.energy / 10f, 1.0f);
			float green = 0.0f;		
			Color healthColour = new Color(red, green, blue);			
			Debugger.drawBounds(g, this.getBounds(), healthColour);
		}
	}

}
