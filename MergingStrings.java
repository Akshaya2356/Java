public class MergingStrings
{
    public static String merge(String s1, String s2) 
    {
        StringBuilder mergedString = new StringBuilder();
        int i = 0, j = 0;
        while (i < s1.length() && j < s2.length()) 
        {
            mergedString.append(s1.charAt(i)).append(s2.charAt(j));
            i++;
            j++;
        }
        if (i < s1.length()) 
        {
            mergedString.append(s1.substring(i));
        }
        if (j < s2.length()) 
        {
            mergedString.append(s2.substring(j));
        }
        return mergedString.toString();
    }
    public static void main(String[] args) 
    {
        String s1 = "abc";
        String s2 = "def";
        String mergedString = merge(s1, s2);
        System.out.println(mergedString);
    }
}
