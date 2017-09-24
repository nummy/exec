/**
* FIlE: Square.java
* AUTHOR:;
* DATE: 2017-09-24
* DESC: Implement a class Sqaure to represent a square:
*       it has a attribute width, it offer methods to calculate the area and perimeter
**/
public class Square{
    private int width;

    /*
    constructor for class
    */
    public Square(int w){
        width = w;
    }

    public void setWidth(int w){
        width = w;
    }


    public int getWidth(){
        return with;
    }

    /*
    return the area of the square
    */
    public int area(){
        return width*width;
    }

    /*
    return the perimeter of the sqaure
    */
    public int perimeter(){
        return width * 4;
    }

    /*
    print instance of the class informatively
    */
    public String toString(){
        return "<Sqaure width=" + width + ">";
    }
}