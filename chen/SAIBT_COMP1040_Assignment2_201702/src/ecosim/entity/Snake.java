package ecosim.entity;


import engine.graphics.ImageLibrary;

public class Snake extends Animal {

	float attackSpeed;
	float moveSpeed;
	Wombat targetWombat;

	public Snake(float x, float y) {
		super(x, y, ImageLibrary.get("snake"), 16, 32, 0.6f);

	}

	@Override
	public void update(long millisElapsed) {
		super.update(millisElapsed);

	}

}
