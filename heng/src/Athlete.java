import java.util.Random;
import java.util.Comparator;
public abstract class Athlete extends Participant{
	private int total_score;
	private int time;
	/**
	 * constructor
	 * @param id  athlete's id
	 * @param name athlete's name
	 * @param state  athlete's state
	 * @param age athlete's age
	 */
	public Athlete(String id, String name, String state, int age) {
		super(id, name, state, age);
	}
	
	/**
	 * abstract method, to be implemented
	 * @return
	 */
	public abstract int complete();
	
	/**
	 * get the total score of the athlete
	 * @return integer
	 */
	public int getTotalScore() {
		return total_score;
	}
	
	/**
	 * set the total score
	 * @param score total score
	 */
	public void setTotalScore(int score) {
		total_score = score;
	}
	
	/**
	 * get the current compete time
	 * @return integer
	 */
	public int getTime() {
		return time;
	}
	
	
	/**
	 * set current compete time
	 * @param time
	 */
	public void setTime(int time) {
		this.time = time;
	}
}

class AthleteComparator implements Comparator<Athlete>{
	/**
	 * compare method
	 */
	public int compare(Athlete o1, Athlete o2) {
		return o1.getTime() - o2.getTime();
	}
}

class Swimmer extends Athlete implements Swimming{
	/**
	 * constructor
	 * @param id Swimmer id
	 * @param name swimmer name
	 * @param state swimmer state
	 * @param age swimmer age
	 */
	public Swimmer(String id, String name, String state, int age) {
		super(id, name, state, age);
	}
	
	/**
	 * implement complete method
	 */
	public int complete() {
		Random r = new Random();
		int time = r.nextInt()%11 + 10;
		this.setTime(time);
		return time;
	}
	
	/**
	 * toString method
	 */
	public String toString() {
		String res = String.format("Swimmer(id=%s, name=%s, state=%s, age=%d, total score=%d)", this.getId(), 
				this.getName(), this.getState(), this.getAge(), this.getTotalScore());
		return  res;
	}
}

class Cyclist extends Athlete implements Cycling{
	/**
	 * constructor for Cyclist
	 * @param id
	 * @param name
	 * @param state
	 * @param age
	 */
	public Cyclist(String id, String name, String state, int age) {
		super(id, name, state, age);
	}
	
	/**
	 * complete method
	 */
	public int complete() {
		Random r = new Random();
		int time = r.nextInt(301)%301 + 500;
		this.setTime(time);
		return time;
	}
	
	/**
	 * return a formated String
	 */
	public String toString() {
		String res = String.format("Cyclist(id=%s, name=%s, state=%s, age=%d, total score=%d)", this.getId(), 
				this.getName(), this.getState(), this.getAge(), this.getTotalScore());
		return  res;
	}
}

class Sprinter extends Athlete implements Running{
	/**
	 * constructor for sprinter
	 * @param id
	 * @param name
	 * @param state
	 * @param age
	 */
	public Sprinter(String id, String name, String state, int age) {
		super(id, name, state, age);
	}
	
	/**
	 * complete method
	 */
	public int complete() {
		Random r = new Random();
		int time = r.nextInt(101)%101 + 100;
		this.setTime(time);
		return time;
	}
	
	/**
	 * return a formated string
	 */
	public String toString() {
		String res = String.format("Sprinter(id=%s, name=%s, state=%s, age=%d, total score=%d)", this.getId(), 
				this.getName(), this.getState(), this.getAge(), this.getTotalScore());
		return  res;
	}
}

class SuperAthlete extends Athlete implements Swimming, Running, Cycling{
	/**
	 * constructor for SuperAthlete
	 * @param id
	 * @param name
	 * @param state
	 * @param age
	 */
	public SuperAthlete(String id, String name, String state, int age) {
		super(id, name, state, age);
	}
	
	/**
	 * complete method
	 */
	public int complete() {
		Random r = new Random();
		int time = r.nextInt(11)%11 + 10;
		this.setTime(time);
		return time;
	}
	
	/**
	 * formated String
	 */
	public String toString() {
		String res = String.format("SuperAthelte(id=%s, name=%s, state=%s, age=%d, total score=%d)", this.getId(), 
				this.getName(), this.getState(), this.getAge(), this.getTotalScore());
		return  res;
	}
}

