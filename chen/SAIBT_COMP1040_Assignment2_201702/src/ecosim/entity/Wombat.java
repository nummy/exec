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
import java.util.Random;
import ecosim.world.Tile;
import engine.GameEngine;
import engine.graphics.ImageLibrary;
import engine.math.Vector2D;
import ecosim.exception.OutOfBoundsException;
public class Wombat extends Animal {
	
	GrassTuft targetGrass;

	public Wombat(float x, float y){
		super(x, y, ImageLibrary.get("wombat"), 10, 18, 1f);
		
	}
	/**
	 * update the wombat
	 */
	@Override
	public void update(long millisElapsed) {
		super.update(millisElapsed);
		if(this.isAlive()) {
			Vector2D position = this.getPosition();
			Vector2D target = this.target;
			if(target != null) {
				double distance = position.distance(target);
				if(distance < Tile.WIDTH/2) {
					// reset target
					this.setTarget(null);
					selectTarget();  // select another target
				}
				
			}
			if(targetGrass !=null) {
				target = targetGrass.getPosition();
				double distance = target.distance(position);
				if(distance<Tile.WIDTH/2) {
					this.setEnergy(this.getEnergy()+10);
					targetGrass.die();
					targetGrass = null;
					selectTarget();  // select another target
				}
			}
		}
	}
	/**
	 * return a new Wombat
	 */
	@Override
	public Animal breed() {
		// TODO Auto-generated method stub
		return new Wombat(this.getX(), this.getY());
	}

	/**
	 * select the closest target grass
	 */
	@Override
	public void selectTarget() {
		// TODO Auto-generated method stub
		if(energy < 10) {
			GrassTuft tuft = this.findGrass();
			if(tuft != null) {
				this.setTarget(tuft.getPosition());
			}
			
		}else {
			if(this.targetGrass == null && this.target == null) {
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
				GrassTuft tuft = new GrassTuft(x,(int)y);
				this.setTarget(tuft.getPosition());
				targetGrass =  tuft;
			}
		}
	}
	
	/**
	 * find the closest GrassTuft
	 * @return
	 */
	public GrassTuft findGrass() {
		GrassTuft guft=null;
		try {
			Object[] objs = GameEngine.getGameObjs("ecosim.entity.GrassTuft");
			if(objs.length > 0) {
				GrassTuft[] tufts = new GrassTuft[objs.length];
				// type cast to GrassTuft
				for(int i=0; i<objs.length; i++) {
					tufts[i] = (GrassTuft)objs[i];
				}
				GrassTuft target = tufts[0];
				double distance = 0;
				Vector2D position = this.getPosition();
				double min = position.distance(tufts[0].getPosition());
				for(int i=0; i<tufts.length; i++) {
					distance = position.distance(tufts[i].getPosition());
					if(distance < min) {
						min = distance;
						target = tufts[i];
					}
				}
				return target;
			}
		}catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		return guft;
	}

}
