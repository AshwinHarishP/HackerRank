import java.util.Scanner;

public class Anagrams {

    static boolean isAnagram(String a, String b) {
        String new_a = a.toLowerCase();
        String new_b = b.toLowerCase(); 
        
        char [] char_a = new_a.toCharArray();
        char [] char_b = new_b.toCharArray();
        
        java.util.Arrays.sort(char_a);
        java.util.Arrays.sort(char_b);
        
        a = new String(char_a);
        b = new String(char_b);
        
        if (a.equals(b)) return true;
        else return false;
        
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
