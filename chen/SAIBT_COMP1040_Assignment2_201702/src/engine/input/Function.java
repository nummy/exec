package engine.input;

/**
 * A KeyFunction can be added to Keyboard keys and Mouse buttons.
 * These buttons will invoke the associated KeyFunction's 
 * execute method when they are pressed.
 * 
 * The KeyFunction can be constructed with a delay. If the delay is set
 * to a number greater than zero, the function will execute again if the 
 * button is held for that many milliseconds. This will repeat while the 
 * button is held. Call the update(long millis), to tell the KeyFunction 
 * how many milliseconds have passed since the last execution. This method
 * is called automatically for each KeyFunction on the Keyboard and Mouse.
 * 
 * To construct a custom KeyFunction, you should define an anonymous class.
 * For example:
 * KeyFunction func = new KeyFunction(){
 * 	@Override
 * 	public void execute(){
 * 		System.out.println("Do something");
 * 	}
 * };
 * 
 * @author Michael
 */
public abstract class Function{

	private boolean pressed;
	private long delay;
	private long timer;

	/**
	 * Constructs a KeyFunction with a delay of zero. The execute function
	 * will be invoked when the key is first pressed. The execute function 
	 * will not be repeated until the key is released and pressed again.
	 */
	public Function(){
		this.pressed = false;
		this.delay = 0;
		this.timer = 0;
	}

	/**
	 * Constructs a KeyFunction with the given delay. The execute function
	 * will be invoked when the key is first pressed. The execute function 
	 * will be repeated every number of milliseconds equal to the delay,
	 * while the key is pressed.
	 * @param delay milliseconds to wait before calling the execute method again.
	 */
	public Function(long delay){
		this.pressed = false;
		this.delay = delay;
		this.timer = delay;
	}
	
	/**
	 * This method is called whenever the key is pressed. It will be called 
	 * from the update() method if the elapsed milliseconds exceeds the delay.
	 * This will continue while the key is pressed.
	 * It may also be called automatically from the press() method.
	 */
	public abstract void execute();

	/**
	 * Updates the KeyFunction's internal timer and calls execute again if
	 * the timer exceeds the delay.
	 * 
	 * This method is automatically called by Mouse and Keyboard.
	 * @param millisElapsed the milliseconds that have passed since the last
	 * invocation of update().
	 */
	public void update(long millisElapsed){
		if(this.delay > 0){
			this.timer += millisElapsed;
			if(this.pressed && this.timer >= this.delay){
				this.execute();
				this.timer = this.timer % this.delay;
			}
		}
	}
	
	/**
	 * Gets the delay associated with the KeyFunction.
	 * @return the delay between calls to execute() in milliseconds.
	 */
	public long getDelay(){
		return this.delay;
	}
	
	/**
	 * Sets the delay between executions of this KeyFunction.
	 * If set to zero, the KeyFunction will only execute once each time
	 * the associated key is pressed.
	 * @param delay a number greater than or equal to zero.
	 */
	public void setDelay(long delay){
		if(delay >= 0){
			this.delay = delay;
		}
	}
	
	/**
	 * Gets the milliseconds since the last execution of this function.
	 * @return Milliseconds since last execution or will be greater than or 
	 * equal to delay if the function is ready for execution.
	 */
	public long getTimer(){
		return this.timer;
	}
	
	/**
	 * This method should be called when the associated key is pressed.
	 * This will automatically call execute if the delay is zero.
	 * If the delay is non-zero, the update method will automatically call
	 * execute instead.
	 */
	public final void press(){
		this.pressed = true;
		if(this.delay == 0){
			this.execute();
		}
	}
	
	/**
	 * This method should be called when the associated key is released.
	 */
	public final void release(){
		this.pressed = false;
	}
	
	/**
	 * Returns true if the key is pressed.
	 * @return true while the key is held down.
	 */
	public final boolean isPressed(){
		return this.pressed;
	}

}
