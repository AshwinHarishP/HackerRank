import java.io.*;
import java.util.*;

public class Java_String_Reverse {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        int r = A.length() - 1;
        int flag = 1;
        
        for (int i = 0; i < (int) A.length() / 2; i++){
            if (A.charAt(i) != A.charAt(r)){
                flag = 0; 
            }
            r --;

        }
        
        if (flag == 1) System.out.println("Yes");
        
        else System.out.println("No");
    }
}



