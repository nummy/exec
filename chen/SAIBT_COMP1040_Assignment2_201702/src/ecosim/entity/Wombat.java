package ecosim.entity;


import engine.graphics.ImageLibrary;

public class Wombat extends Animal {
	
	GrassTuft targetGrass;

	public Wombat(float x, float y){
		super(x, y, ImageLibrary.get("wombat"), 10, 18, 1f);

	}

	@Override
	public void update(long millisElapsed) {
		super.update(millisElapsed);	
		
		this.getBounds().move(1, 0);
	}

}
