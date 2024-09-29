import java.util.HashSet;
import java.util.Set;

public class CheckPangram
{
    public static void main(String s[]) 
    {
        String sentence = "The quick brown fox jumps over the lazy Dog.";
        if (isPangram(sentence)) 
        {
            System.out.println(1);
        }
        else 
        {
            System.out.println(-1);
        }
    }
    public static boolean isPangram(String sentence) 
    {
        Set<Character> alphabet = new HashSet<>();
        for (char c = 'a'; c <= 'z'; c++) 
        {
            alphabet.add(c);
        }
        for (char c : sentence.toLowerCase().toCharArray()) 
        {
            if (c >= 'a' && c <= 'z') 
            {
                alphabet.remove(c);
            }
        }
        return alphabet.isEmpty();
    }
}
