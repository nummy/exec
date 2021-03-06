package ecosim.entity;
/**  
/ File: fileName.java 
/ Author: your name  
/ Id: your id  
/ Version: 1.0 today��s date  
/ Description: Assignment 2 - ��.  
/ This is my own work as defined by the SAIBT 
/ Academic Misconduct policy.  
*/  

import java.util.Random;

import ecosim.exception.OutOfBoundsException;
import ecosim.world.Tile;
import engine.GameEngine;
import engine.graphics.ImageLibrary;
import engine.math.Vector2D;

public class Snake extends Animal {

	float attackSpeed;
	float moveSpeed;
	Wombat targetWombat;

	public Snake(float x, float y) {
		super(x, y, ImageLibrary.get("snake"), 16, 32, 0.6f);
		attackSpeed = 1.1f;
		moveSpeed = 2f;
		
	}
	/**
	 * update the Snake when it is alive, call the super update method
	 */
	@Override
	public void update(long millisElapsed) {
		super.update(millisElapsed); // call super update method
		if(this.isAlive()) { 
			// if the snake is alive
			// update the speed
			this.setSpeed(moveSpeed);
			if((targetWombat != null) && targetWombat.isAlive()) {
				// if the target exists and target is alive
				target = targetWombat.getPosition();
				double distance = target.distance(this.getPosition());
				if(distance<Tile.WIDTH/2) {
					// remove the target wombat
					this.setEnergy(this.getEnergy() + targetWombat.getEnergy());
					targetWombat.die();
					targetWombat = null;
				}
				if(distance<Tile.WIDTH*3) {
					// update speed
					this.setSpeed(attackSpeed);
				}
				// reselect a new target
				selectTarget();
			}
		}
	}
	/**
	 * breed a new animal
	 */
	@Override
	public Animal breed() {
		// TODO Auto-generated method stub
		return new Snake(this.getX(), this.getY());
	}
	/*
	 *  select a new target
	 */
	@Override
	public void selectTarget() {
		// TODO Auto-generated method stub
		// find the target when energy less than 8
		if(energy < 8) {
			Wombat wombat = this.findWombat();
			if(wombat !=null) {
				this.setTarget(wombat.getPosition());
			}
		}else {
			// generate a new target and handle out of bounds exception
			Vector2D position = this.getPosition();
			Random r = new Random();
			int x = r.nextInt(150);
			int sign = r.nextInt(2);
			if(sign == 0) {
				x = -x;
			}
			double y = Math.sqrt(150*150-x*x);
			sign = r.nextInt(2);
			if(sign == 0) {
				y = -y;
			}
			try {
				if(x<0 || y<0 || x > GameEngine.getGame().getWinWidth() || y > GameEngine.getGame().getWinHeight()){
					Vector2D bad = new Vector2D((float)x,(float)y);
					throw new OutOfBoundsException(bad);
				}
			}catch(OutOfBoundsException e) {
				if(x<0) {
					x=0;
				}
				if(y<0) {
					y=0;
				}
				if(x>GameEngine.getGame().getWinWidth()) {
					x= GameEngine.getGame().getWinWidth();
				}
				if(y > GameEngine.getGame().getWinHeight()) {
					y = GameEngine.getGame().getWinHeight();
				}
			}
			Wombat wombat = new Wombat(x,(int)y);
			this.setTarget(wombat.getPosition());
			targetWombat =  wombat;
		}
	}
	/**
	 * find the closest wombat
	 * @return
	 */
	public Wombat findWombat() {
		Wombat wombat=null;
		try {
			// get all the wombats
			Object[] objs = GameEngine.getGameObjs("ecosim.entity.Wombat");
			if(objs.length >0) {
				Wombat[] wombats = new Wombat[objs.length];
				// type cast to GrassTuft
				for(int i=0; i<objs.length; i++) {
					wombats[i] = (Wombat)objs[i];
				}
				Wombat target = wombats[0];
				double distance = 0;
				Vector2D position = this.getPosition();
				double min = position.distance(wombats[0].getPosition());
				// get the closest wombat
				for(int i=0; i<wombats.length; i++) {
					distance = position.distance(wombats[i].getPosition());
					if(distance < min) {
						min = distance;
						target = wombats[i];
					}
				}
				return target;
			}
		}catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		return wombat;
	}

}
