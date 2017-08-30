package engine.graphics;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;

import javax.imageio.ImageIO;

/**
 * ImageLibrary is a static singleton class. The ImageLibrary cannot be 
 * constructed and only the static methods can be accessed. This class
 * acts as a place to store BufferedImages so that they can be loaded 
 * and accessed from anywhere. Rather than accessing the image by index, 
 * these images can be accessed by a name. This name can be specified in
 * the alias parameter for ImageLibrary.load(String alias, String path).
 * 
 * Call ImageLibrary.load(String alias, String path) from your Game.load() method.
 * You should call this method once for each image your game needs to access.
 * For example:
 * ImageLibrary.load("wombat", "assets/images/wombat1.png");
 * ImageLibrary.load("snake", "assets/images/snake1.png");
 * 
 * The images can then be accessed by calling ImageLibrary.get(String alias).
 * For example:
 * BufferedImage wombatImg = ImageLibrary.get("wombat");
 * 
 * @author Michael
 */
public class ImageLibrary {
	
	private static HashMap<String, BufferedImage> images = new HashMap<String, BufferedImage>();

	private ImageLibrary(){ }	//Cannot be constructed
	
	/**
	 * Reads the image path as a BufferedImage and saves it, mapped to the given alias.
	 * @param alias the name to access the image with.
	 * @param imagePath a relative path to the location of the image file on the computer.
	 */
	public static void load(String alias, String imagePath){
		try{
			images.put(alias, ImageIO.read(new File(imagePath)));
		}
		catch(IOException e){
			e.printStackTrace();
		}
	}
	
	/**
	 * Accesses the image mapped to the given alias and returns it.
	 * @param alias The name mapped to the required BufferedImage.
	 * @return the BufferedImage mapped to the given alias or null if unmapped.
	 */
	public static BufferedImage get(String alias){
		return images.get(alias);
	}
}
