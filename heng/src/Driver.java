import java.util.*;

public class Driver {
	private Athlete predict_winner; 
	private Athlete winner;
	private ArrayList<Game> games = new ArrayList<Game>(); // use an ArrayList to store all the games;
	private ArrayList<Athlete> athletes = new ArrayList<Athlete>(); // use an ArrayList to store all the athletes
	private Game current_game;
	
	/**
	 * show the main menu
	 */
	public static void showMenu() {
		System.out.println("Ozlympic Game");
		System.out.println("===================================");
		System.out.println("1.Select a game to run");
		System.out.println("2.Predict the winner of the game");
		System.out.println("3.Start the game");
		System.out.println("4.Display the final results of all games");
		System.out.println("5.Display the points of all athletes");
		System.out.println("6.Exit");
	}
	
	
	/**
	 * handle input choice
	 * @param choice
	 */
	public void handleChoice(int choice) {
		switch(choice) {
			case 1:
				selectGame();
				break;
			case 2:
				handlePredict();
				break;
			case 3:
				startGame();
				break;
			case 4:
				displayGameResult();
				break;
			case 5:
				displayAthletePoint();
				break;
		}
	}
	
	/**
	 * start the game
	 */
	public void startGame() {
		System.out.println("\n=========================================");
		if(current_game == null) {
			System.out.println("\nPlease select a game at first\n");
			return;
		}
		if(predict_winner == null) {
			System.out.println("\nPlease predict the winner before game start\n");
			return;
		}
		winner = current_game.startGame();
		if(predict_winner == winner) {
			System.out.println("Congratulations, You won!");
			System.out.println("The winner is" + winner.toString());
		}else {
			System.out.println("Sorry, you lose!");
		}
		System.out.println("The winner is" + winner.toString());
		System.out.println();
		predict_winner = null;
		winner = null;
		current_game = null;
	}
	
	/**
	 * display the game result
	 */
	public void displayGameResult() {
		System.out.println("\n=========================================");
		for(int i=0; i<games.size(); i++) {
			Game game = games.get(i);
			ArrayList<Athlete> athletes = new ArrayList<Athlete>();
			athletes = game.getAthletes();
			System.out.printf("\nThe %s(%s)'s result is:\n", game.getGameType(), game.getId());
			for(int j=0; j<athletes.size(); j++) {
				Athlete athlete = athletes.get(j);
				System.out.printf("Rank %d: %s(%s) %s\n", i+1, athlete.getName(), athlete.getId(), athlete.getTime());
			}
			System.out.println("");
		}
	}
	
	/**
	 * display the athlete's point
	 */
	public void displayAthletePoint() {
		System.out.println("\n=========================================");
		System.out.println("\nThe points of all the athletes are list as below:");
		for(int i=0; i<athletes.size(); i++) {
			Athlete athlete = athletes.get(i);
			System.out.printf("%s(%s): point=%d\n", athlete.getName(), athlete.getId(), athlete.getTotalScore());
		}
		System.out.println();
	}
	
	/**
	 * predict the winner
	 */
	public void handlePredict() {
		System.out.println("\n=========================================");
		if(current_game == null) {
			System.out.println("\nPlease select a game at first\n");
			return;
		}
		System.out.println("\nPlease select the winner's ID from the list below:");
		ArrayList<Athlete> athletes = current_game.getAthletes();
		for(int i=0; i<athletes.size(); i++) {
			System.out.println(athletes.get(i).getId() + ":" + athletes.get(i).getName());
		}
		Scanner scan = new Scanner(System.in);
		String choice;
		boolean flag;
		Athlete athlete = null;
		while(true) {
			choice = scan.nextLine();
			athlete = findAthlete(current_game.getAthletes(), choice);
			if(athlete != null) {
			    predict_winner = athlete;
			    System.out.println("\nThe predict winner is:");
			    System.out.println(athlete.toString());
			    System.out.println();
			    break;
			}else {
			    System.out.println("\nThe id is not in this list, please input again\n");
			}
			for(int i=0; i<athletes.size(); i++) {
				System.out.println(athletes.get(i).getId() + ":" + athletes.get(i).getName());
			}
		}
		
	}
	
	/**
	 * find the athlete by id
	 * @param athletes
	 * @param id
	 * @return
	 */
	public Athlete findAthlete(ArrayList<Athlete> athletes, String id) {
		Athlete athlete = null;
		for(int i=0; i<athletes.size(); i++) {
			if(athletes.get(i).getId().equals(id)) {
				return athletes.get(i);
			}
		}
		return athlete;
	}
	
	/**
	 * select a game to start
	 */
	public void selectGame() {
		System.out.println("\n===========================");
		System.out.println("Please select a game to run:");
		for(int i=0; i<games.size(); i++) {
			System.out.println(games.get(i).getId() + ":" + games.get(i).getGameType());
		}
		Scanner scan = new Scanner(System.in);
		String choice;
		Game game = null;
		while(true) {
			choice = scan.nextLine();
			game = findGame(choice);
			if(game == null) {
				System.out.println("\nNo such choice, Please select again!");
				for(int i=0; i<games.size(); i++) {
					System.out.println(games.get(i).getId() + ":" + games.get(i).getGameType());
				}
			}else {
				current_game = game;
				System.out.printf("\nGame %s:%s was selected\n", game.getId(), game.getGameType());
				System.out.println();
				break;
			}
		}
	}
	
	/**
	 * find the game to start
	 * @param gid
	 * @return
	 */
	public Game findGame(String gid) {
		Game game = null;
		for(int i=0; i< games.size(); i++) {
			if(games.get(i).getId().equals(gid)) {
				game = games.get(i);
			}
		}
		return game;
	}
	
	
	/**
	 * get input data and init it
	 */
	public void init() {
		//NSW	VIC	QLD	SA	WA	TAS	NT	ACT
		String[] names = {"Jim", "Kate", "Tom", "Aaron", "Allen", "Wang", "Abel", "Adam", 
				"Alva", "Alan", "Dedek", "David", "Jack", "James", "Jacob", "Warren", "Abby", 
				"Ada", "Balanche", "Candice", "Eva", "Joy"};
		String[] states = {"NSW", "VIC", "QLD", "WA", "SA", "TAS", "NT", "ACT"};
		Official official1 = new Official("o01", "Lucy", "TAS", 40);
		Official official2 = new Official("o02", "Melody", "ACT", 50);
		Official official3 = new Official("o03", "Polly", "QLD", 35);
		Game game1 = new Game("S01", official1);
		Game game2 = new Game("C01", official2);
		Game game3 = new Game("R01", official3);
		games.add(game1);
		games.add(game2);
		games.add(game3);
		Random r = new Random();
		for(int i=1; i<=6; i++) {
			String sId = "s" + String.valueOf(i);
			String rId = "r" + String.valueOf(i);
			String cId = "c" + String.valueOf(i);
			Swimmer swimmer = new Swimmer(sId, names[r.nextInt(names.length)], states[r.nextInt(states.length)], r.nextInt(5) + 18);
			Cyclist cyclist = new Cyclist(cId, names[r.nextInt(names.length)], states[r.nextInt(states.length)], r.nextInt(5) + 18);
			Sprinter sprinter = new Sprinter(rId, names[r.nextInt(names.length)], states[r.nextInt(states.length)], r.nextInt(5) + 18);
			game1.addAthlete(swimmer);
			game2.addAthlete(cyclist);
			game3.addAthlete(sprinter);
			athletes.add(swimmer);
			athletes.add(cyclist);
			athletes.add(sprinter);
		}
		SuperAthlete athlete1 = new SuperAthlete("super01", "Eva", "ACT", 23);
		SuperAthlete athlete2 = new SuperAthlete("super02", "Jack", "WA", 22);
		game1.addAthlete(athlete1);
		game1.addAthlete(athlete2);
		game2.addAthlete(athlete1);
		game2.addAthlete(athlete2);
		game3.addAthlete(athlete1);
		game3.addAthlete(athlete2);
		athletes.add(athlete1);
		athletes.add(athlete2);
	}
	
	/**
	 * start the main function
	 */
	public void start() {
		init();
		int choice = 0;
		boolean  flag;
		Scanner keyboard = new Scanner(System.in);
		showMenu();
		System.out.print("Enter an option:");
		while(true) {
			flag = false;
			if(keyboard.hasNextInt()) {
				choice = keyboard.nextInt();
				if(choice == 6) {
					flag = true;
					break;
				}
				if(choice >= 1 && choice <=5) {
					handleChoice(choice);
				}else {
					System.out.println("\nNo such choice, please input again\n");
				}
			}else {
				System.out.println("\nNo such choice, please input again\n");
			}
			if(flag) {
				break;
			}
			showMenu();
			System.out.print("Enter an option:");
		}
	}
}
