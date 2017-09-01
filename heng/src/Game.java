import java.util.ArrayList;

public class Game {
	String id;
	Official referee; 
	ArrayList<Athlete> athletes = new ArrayList<Athlete>();
	/**
	 * constructor for the game
	 * @param id
	 * @param o
	 */
	public Game(String id, Official o) {
		referee = o;
		this.id = id;
	}
	
	/**
	 * add athlete
	 * @param athlete
	 * @return
	 */
	public boolean addAthlete(Athlete athlete) {
		if(athletes.size()==8) {
			return false;
		}else {
			athletes.add(athlete);
			return true;
		}
	}
	
	/**
	 * get all the athletes
	 * @return
	 */
	public ArrayList<Athlete> getAthletes() {
		return athletes;
	}
	
	/**
	 * start the game
	 * @return
	 */
	public Athlete startGame() {
		int time;
		Athlete winner = null;
		for(int i=0; i<athletes.size(); i++) {
			time = athletes.get(i).complete();
		}
		AthleteComparator comparator =  new AthleteComparator();
		athletes.sort(comparator);
		winner = athletes.get(0);
		athletes.get(0).setTotalScore(athletes.get(0).getTotalScore() + 5);
		athletes.get(1).setTotalScore(athletes.get(1).getTotalScore() + 2);
		athletes.get(2).setTotalScore(athletes.get(2).getTotalScore() + 1);
		System.out.println("\nThe game finished:\n");
		System.out.printf("%-6s:%-10s %-10s %-10s %-10s\n", "Rank", "ID", "NAME", "STATE", "TIME");
		for(int j=0; j<athletes.size(); j++) {
			Athlete athlete = athletes.get(j);
			System.out.printf("Rank%-2s: %-10s %-10s %-10s %-10d\n", j, athlete.getId(), athlete.getName(), athlete.getState(), athlete.getTime());
		}
		System.out.println();
		return winner;
	}
	
	/**
	 * get the game id
	 * @return
	 */
	public String getId() {
		return id;
	}
	
	/**
	 * get the game type
	 * @return
	 */
	public String getGameType() {
		if(id.startsWith("S")) {
			return "Swimming";
		}else if(id.startsWith("R")) {
			return "Sprinter";
		}else {
			return "Cyclist";
		}
	}
	
}

