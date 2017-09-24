/**
*
**/
public class Square{
    private int width;
    public Square(int w){
        width = w;
    }

    public void setWidth(int w){
        width = w;
    }

    public int getWidth(){
        return with;
    }

    public int area(){
        return width*width;
    }

    public int perimeter(){
        return width * 4;
    }

    public String toString(){
        return "<Sqaure width=" + width + ">";
    }
}