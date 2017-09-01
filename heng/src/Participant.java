
public class Participant {
	private String id;
	private String name;
	private String state;
	private int age;
	/*
	 * constructor for the Participant
	 */
	public Participant(String id, String name, String state, int age) {
		this.id = id;
		this.name = name;
		this.state = state;
		this.age = age;
	}
	
	/**
	 * get the id
	 * @return
	 */
	public String getId() {
		return id;
	}
	
	/**
	 * get the name
	 * @return
	 */
	public String getName() {
		return name;
	}
	
	/**
	 * get the state
	 * @return
	 */
	public String getState() {
		return state;
	}
	
	/*
	 * get the age
	 */
	public int getAge() {
		return age;
	}	
}
