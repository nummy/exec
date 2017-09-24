public class Test{
    public static void main(String []args){
        Square s1 = new Square(2);
        Square s2 = new Square(3);
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s1.area());
        System.out.println(s1.perimeter());
        System.out.println(s2.area());
        System.out.println(s2.perimeter());
        s2.setWidth(5);
        System.out.println(s2);
        System.out.println(s2.area());
        System.out.println(s2.perimeter());
    }
}