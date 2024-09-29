class AreaOfShapes 
{
    public static void main(String[] args) 
    {
        Shape obj1 = new Rectangle(10, 20);
        obj1.printArea(); 
        Shape obj2 = new Triangle(30, 40);
        obj2.printArea();
        Shape obj3 = new Circle(1);
        obj3.printArea();  
    }
}
abstract class Shape 
{
    int a;
    int b;
    public Shape(int a, int b) 
    {
        this.a = a;
        this.b = b;
    }
    abstract void printArea();
}
class Rectangle extends Shape 
{
    public Rectangle(int a, int b) 
    {
        super(a, b);
    }
    void printArea() 
    {
        System.out.println("Area of Rectangle is: " + (a * b));
    }
}
class Triangle extends Shape 
{
    public Triangle(int a, int b) 
    {
        super(a, b);
    }
    void printArea() 
    {
        System.out.println("Area of Triangle is: " + (0.5 * a * b));
    }
}
class Circle extends Shape 
{
    public Circle(int r) 
    {
        super(r, 0); 
    }
    void printArea() 
    {
        System.out.println("Area of Circle is: " + (3.14 * a * a)); 
    }
}
