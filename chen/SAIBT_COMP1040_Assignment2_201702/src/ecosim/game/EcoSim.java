package ecosim.game;
/**  
/ File: fileName.java 
/ Author: your name  
/ Id: your id  
/ Version: 1.0 today¡¯s date  
/ Description: Assignment 2 - ¡­.  
/ This is my own work as defined by the SAIBT 
/ Academic Misconduct policy.  
*/  
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.IOException;
import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

import javax.imageio.ImageIO;

import ecosim.entity.Entity;
import ecosim.entity.GrassTuft;
import ecosim.entity.Snake;
import ecosim.entity.Wombat;
import ecosim.world.GrassTile;
import ecosim.world.SandTile;
import ecosim.world.Tile;
import engine.Game;
import engine.GameEngine;
import engine.graphics.Debugger;
import engine.graphics.ImageLibrary;
import engine.input.Function;
import engine.input.Keyboard;
import engine.input.Mouse;
import engine.interfaces.IPaintable;
import engine.interfaces.IUpdatable;
import engine.math.BoundingBox;
import engine.math.Vector2D;


public class EcoSim extends Game{

	private Tile[][] tiles;
	int gridWidth;
	int gridHeight;
	int timer = 0;

	/**
	 * constructor for the EcoSim
	 * @param gridWidth
	 * @param gridHeight
	 */
	public EcoSim(int gridWidth, int gridHeight){
		this.gridHeight = gridHeight;
		this.gridWidth = gridWidth;
		tiles = new Tile[gridWidth][gridHeight];
	}
	/**
	 * create tiles and animals, add they to the GameEngine.
	 */
	@Override
	public void load(){
		int number;
		Random r = new Random();
		super.load();
		Tile tile;
		for(int i=0; i< gridWidth; i++) {
			for(int j=0; j<gridHeight; j++) {
				number = r.nextInt(10);
				if(number<8) {
					tile = new GrassTile(i*Tile.WIDTH, j*Tile.HEIGHT);
					GameEngine.addToBackground(tile);
					tiles[i][j] = tile;
					number = r.nextInt(10);
					if(number<5) {
						GameEngine.add(new GrassTuft(i*Tile.WIDTH, j*Tile.HEIGHT));
					}
					
				}else {
					tile = new SandTile(i*Tile.WIDTH, j*Tile.HEIGHT);
					GameEngine.addToBackground(tile);
					tiles[i][j] = tile;
				}
				number = r.nextInt(10);
				if(number<2) {
					GameEngine.add(new Wombat(i*Tile.WIDTH, j*Tile.HEIGHT));
				}else if(number <3) {
					GameEngine.add(new Snake(i*Tile.WIDTH, j*Tile.HEIGHT));
				}
			}
		}

	}
	/**
	 *  Add a GrassTuft object to the GameEngine background every 1000 milliseconds
	 */
	@Override
	public void update(long millisElapsed) {
		timer = timer + (int)millisElapsed;
		GrassTile[] grass = new GrassTile[gridWidth*gridHeight];
		float x1,x2,y1,y2;
		int counter = 0;
		boolean found;
		if(timer > 1000) {
			try {
				Object[] objs = GameEngine.getGameObjs("ecosim.entity.GrassTuft");
				GrassTuft[] tufts = new GrassTuft[objs.length];
				// type cast to GrassTuft
				for(int i=0; i<objs.length; i++) {
					tufts[i] = (GrassTuft)objs[i];
				}
				for(int i=0;i<gridWidth; i++) {
					for(int j=0; j<gridHeight; j++) {
						Tile tile= tiles[i][j];
						x1 = tile.getX();
						y1 = tile.getY();
						if(tile.getClass() == GrassTile.class) {
							found = false;
							for(int k=0; k<tufts.length; k++) {
								x2 = tufts[k].getX();
								y2 = tufts[k].getY();
								if(x1==x2 && y1==y2) {
									found = true;
									break;
								}
							}
							if(!found) {
								grass[counter] = (GrassTile)tile;
								counter++;
							}
						}
					}
				}
				if(counter>=1) {
					// add new GrassTuft
					Random r = new Random();
					int num = r.nextInt(counter);
					GrassTile tile = grass[num];
					GrassTuft tuft = new GrassTuft(tile.getX(),tile.getY());
					GameEngine.add(tuft);
					// reset to zero
					timer = 0;
				}
			}catch (ClassNotFoundException e) {
				e.printStackTrace();
			}
		}
	}
	
	
	/**
	 * Loads the standard EcoSim images to the ImageLibrary.
	 * You can access the images using their alias.
	 * For example: 
	 * BufferedImage wombat = ImageLibrary.get("wombat");
	 * BufferedImage wombat = ImageLibrary.get("snake");
	 * BufferedImage grasstile = ImageLibrary.get("grass_tile");
	 * BufferedImage grassObj = ImageLibrary.get("grass_tuft");
	 */
	public void loadImages(){
		ImageLibrary.load("grass_tile", "assets/images/grass_tile.png");
		ImageLibrary.load("sand_tile", "assets/images/sand_tile.png");
		ImageLibrary.load("grass_tuft", "assets/images/grass_tuft.png");
		ImageLibrary.load("wombat", "assets/images/wombat1.png");
		ImageLibrary.load("snake", "assets/images/snake1.png");
	}

	/**
	 * Loads the standard keyboard functions:
	 * Press these keys to perform the following functions:
	 * Escape 			= 	QUIT
	 * Space 			= 	PAUSE
	 * Tilde 			= 	DEBUG
	 * Left Control		= 	PAUSE/STEP
	 */
	@Override
	public void loadKeyFunctions() {
		Keyboard.setKeyFunction(KeyEvent.VK_ESCAPE, new Function(){
			@Override
			public void execute() {

				GameEngine.quit();
			}
		});		

		Keyboard.setKeyFunction(KeyEvent.VK_SPACE, new Function(){
			@Override
			public void execute() {
				GameEngine.togglePaused();
			}
		});

		Keyboard.setKeyFunction(Keyboard.LEFT_CTRL, new Function(150){
			@Override
			public void execute() {
				GameEngine.pause(true);
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				GameEngine.update(200);
			}
		});

		Keyboard.setKeyFunction(KeyEvent.VK_BACK_QUOTE, new Function(){
			@Override
			public void execute() {
				GameEngine.toggleDebug();
			}
		});
	}

	/**
	 * Loads the standard Mouse functions.
	 * Press these buttons to perform these functions:
	 * Left Click	=	Spawn Wombat
	 * Right Click	= 	Spawn Snake
	 * Middle Click	=	Spawn Grass
	 */
	@Override
	public void loadMouseFunctions(){
		Mouse.setLeftFunction(new Function(){
			@Override
			public void execute() {
				Vector2D pos = Mouse.getLastPos();
				GameEngine.add(new Wombat(pos.getX() - Tile.WIDTH/2,
						pos.getY() - Tile.HEIGHT/2));
			}
		});
		Mouse.setRightFunction(new Function(){
			@Override
			public void execute() {
				Vector2D pos = Mouse.getLastPos();
				GameEngine.add(new Snake(pos.getX() - Tile.WIDTH/2,
						pos.getY() - Tile.HEIGHT/2));
			}
		});
		Mouse.setMiddleFunction(new Function(){
			@Override
			public void execute() {
				Vector2D mousePos = Mouse.getLastPos();
				Vector2D gridPos = new Vector2D((int)(mousePos.getX()/Tile.WIDTH), (int)(mousePos.getY()/Tile.HEIGHT));
				try {
					Object[] objs = GameEngine.getGameObjs("ecosim.entity.GrassTuft");
					if(tiles[(int)gridPos.getY()][(int)gridPos.getX()].getClass() == GrassTile.class){
						boolean posTaken = false;
						for(int i=0; i<objs.length && posTaken == false; i++){
							GrassTuft grass = (GrassTuft)objs[i];
							if(grass.getX() == gridPos.getX() && grass.getY() == gridPos.getY()){
								posTaken = true;
							}
						}
						if(!posTaken){
							GameEngine.addToBackground(new GrassTuft(
									gridPos.getX() * Tile.WIDTH, gridPos.getY() * Tile.HEIGHT));
						}
					}
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
		});
	}
	/** 
	   * Return the total screen width of the Game, which should be 
	   * the number of horizontal Tiles multiplied by the tile width.  
	   * @return gridWidth multiplied by default Tile width. 
	   */ 
	@Override
	public int getWinWidth() {
		return this.gridWidth * Tile.WIDTH;
	}
	/** 
	   * Return the total screen height of the Game, which should be 
	   * the number of vertical Tiles multiplied by the tile height.  
	   * @return gridHeight multiplied by default Tile height. 
	   */ 
	@Override
	public int getWinHeight() {
		return this.gridHeight * Tile.HEIGHT;
	}
}
