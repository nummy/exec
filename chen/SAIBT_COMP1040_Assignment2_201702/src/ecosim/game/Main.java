package ecosim.game;

import engine.GameEngine;

/**
 * This is the starting point of the project.
 * Execute this main method to open the application.
 * @author Michael
 */
public class Main {

	public static void main(String[] args){
		EcoSim g = new EcoSim(12, 10);
		GameEngine.loadGame(g);
	}
	
}
