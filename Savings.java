public class SavingsAccount 
{
    private static double annualInterestRate;
    private double savingsBalance;
    public SavingsAccount(double initialBalance) 
    {
        if (initialBalance >= 0) 
        {
            this.savingsBalance = initialBalance;
        } 
        else 
        {
            this.savingsBalance = 0;
        }
    }
    public void calculateMonthlyInterest() 
    {
        double monthlyInterest = (savingsBalance * annualInterestRate) / 12;
        savingsBalance += monthlyInterest;
    }
    public static void modifyInterestRate(double newRate) 
    {
        annualInterestRate = newRate;
    }
    public double getSavingsBalance()
    {
        return savingsBalance;
    }

}

public class Savings 
{
    public static void main(String[] args) 
    {
        SavingsAccount.modifyInterestRate(0.04);
        SavingsAccount account1 = new SavingsAccount(1000.00);
        account1.calculateMonthlyInterest();
        System.out.println("Savings Balance after interest: " + account1.getSavingsBalance());
        SavingsAccount.modifyInterestRate(0.05);
        SavingsAccount account2 = new SavingsAccount(2000.00);
        account2.calculateMonthlyInterest();
        System.out.println("Savings Balance after interest: " + account2.getSavingsBalance());
    }
}
