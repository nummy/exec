package ecosim.entity;
/**  
/ File: fileName.java 
/ Author: your name  
/ Id: your id  
/ Version: 1.0 today¡¯s date  
/ Description: Assignment 2 - ¡­.  
/ This is my own work as defined by the SAIBT 
/ Academic Misconduct policy.  
*/  
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;

import engine.GameEngine;
import engine.math.Vector2D;
import engine.graphics.Debugger;

public abstract class Animal extends Entity{

	private int timer;
	protected int energy;
	protected int maxBreedTime;
	protected int breedTime;
	protected float speed;
	/**
	 * constructor for the class Animal
	 * @param x
	 * @param y
	 * @param image
	 * @param energy
	 * @param breedSteps
	 * @param moveSpeed
	 */
	public Animal(float x, float y, BufferedImage image, 
			int energy, int breedSteps, float moveSpeed) {
		super(x, y, image);
		this.selectTarget();
		this.energy = energy;
		this.speed = moveSpeed;
		this.maxBreedTime = breedSteps;
		this.breedTime = breedSteps;
		this.timer = 0;
	}

	public abstract Animal breed();
	
	public abstract void selectTarget();
	
	@Override
	public void update(long millisElapsed) {
		this.timer += millisElapsed;
		if(timer > 1000) {
			// if timer > 1000, then update operation
			energy--;  // decrease one
			breedTime--;  // decrease one
			if(energy<=0) {
				this.die();
			}else {
				// breed a new animal
				if(breedTime<=0) {
					Animal an= this.breed();
					GameEngine.add(an);
					breedTime = maxBreedTime;
				}
				//move to next target when it is alive
				if(this.isAlive()) {
					//move to next target
					Vector2D target = this.target;
					if(target != null) {
						Vector2D direction = target.clone().subtract(this.getPosition());
						direction.normalize().scale(this.speed); 
						this.getBounds().move(direction); 
					}
				}
			}
			timer = 0;
		}
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
	/**
	 * Get the energy
	 * @return energy
	 */
	public int getEnergy() {
		return energy;
	}
	
	/**
	 * set the energy
	 * @param e
	 */
	public void setEnergy(int e) {
		if(e>=0) {
			energy = e;
		}
	}
	/**
	 * get the breed time
	 * @return
	 */
	public int getBreedTime() {
		return breedTime;
	}
	/**
	 * set the breed time
	 * @param b
	 */
	public void setBreedTime(int b) {
		if(b>=0) {
			breedTime = b;
		}
	}
	/**
	 * get the max breed time
	 * @return
	 */
	public int getMaxBreedTime() {
		return maxBreedTime;
	}
	/**
	 * set the max breed time
	 * @param m
	 */
	public void setMaxBreedTime(int m) {
		// update only m > 0
		if(m>=0) {
			this.maxBreedTime = m;
		}
	}
	/**
	 * set the speed
	 * @param s
	 */
	public void setSpeed(float s) {
		// update only when s > 0
		if(s>=0) {
			this.speed = s;
		}
	}
	/**
	 * get the speed
	 * @return
	 */
	public float getSpeed() {
		return this.speed;
	}

}
