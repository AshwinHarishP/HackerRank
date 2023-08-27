import java.io.*;
import java.util.*;

public class String_tokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.
        s = s.trim();
        if (s.isEmpty()) System.out.println(0);
        
        else{
            
            String[] new_S = s.split("[\\s?!._,@?']+");
            System.out.println(new_S.length);
                        
            for (String i:new_S) System.out.println(i);
        }
        scan.close();
    }
}

