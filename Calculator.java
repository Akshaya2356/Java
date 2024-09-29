import java.util.*;
public class Calculator 
{
    public static void main(String s[]) 
    {
        Scanner sc = new Scanner(System.in);
        try {
              System.out.print("Enter operand 1: ");
              double num1 = Double.parseDouble(sc.nextLine());
              System.out.print("Enter operand 2: ");
              double num2 = Double.parseDouble(sc.nextLine());
              System.out.print("Enter the operator (+, -, *, /, %): ");
              char op = sc.nextLine().charAt(0);
              double result;
              switch (op) 
              {
                  case '+':
                      result = num1 + num2;
                      break;
                  case '-':
                      result = num1 - num2;
                      break;
                  case '*':
                      result = num1 * num2;
                      break;
                  case '/':
                      if (num2 == 0)
                      {
                          throw new ArithmeticException("Cannot divide by zero.");
                      }
                      result = num1 / num2;
                      break;
                  case '%':
                      result = num1 % num2;
                      break;
                  default:
                      System.out.println("Invalid Operator");
              }

              System.out.println("Result: " + result);
        } 
        catch (NumberFormatException e) 
        {
            System.out.println("Please enter valid numbers.");
        } 
        catch (ArithmeticException e) 
        {
            System.out.println("A Number cannot be divided by 0.Please enter other number.");
        }
    }
}
