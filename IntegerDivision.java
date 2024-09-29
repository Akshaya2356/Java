import java.util.*;
public class IntegerDivision 
{
    public static void main(String s[]) 
    {
        Scanner sc = new Scanner(System.in);
        try 
        {
            System.out.print("Enter Num1: ");
            int num1 = Integer.parseInt(sc.nextLine());
            System.out.print("Enter Num2: ");
            int num2 = Integer.parseInt(sc.nextLine());
            if (num2 == 0) 
            {
                throw new ArithmeticException("Cannot divide by zero.");
            }
            int result = num1 / num2;
            System.out.println("Result: " + result);
        } 
        catch (NumberFormatException e) 
        {
            System.out.println("Please enter integers only.");
        } 
        catch (ArithmeticException e1) 
        {
            System.out.println(e1.getMessage());
        }
    }
}
