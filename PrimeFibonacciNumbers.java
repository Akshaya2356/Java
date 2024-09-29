public class PrimeFibonacciNumbers
{
    public static void main(String s[]) 
    {
        int max = 100000;
        boolean[] isprime=new boolean[max+1];
        for(int i=2;i<max;i++)
        {
            isprime[i] = true;
            if(i==2)
            {
                isprime[i] = true;
            }
            for(int j=2;j<i;j++)
            {
                if(i%j==0)
                {
                    isprime[i] = false;
                    break;
                }
            }
        }
        int[] fib=new int[max];
        int f0=0,f1=1;
        int f2=0;
        int l=0;
        while(f2<max)
        {
            f2 = f0 + f1;
            fib[l]=f2;
            f0 = f1;
            f1 = f2;
            l++;
        }
        System.out.println("Prime Fibonacci numbers below " + max + ":");
        for (int m = 0; m < l; m++) 
        {
            if (fib[m]<max && isprime[fib[m]]) 
            {
                System.out.print(fib[m] + " ");
            }
        }
    }
}
