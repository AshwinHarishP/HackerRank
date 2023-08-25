import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int H = sc.nextInt();
        int B = sc.nextInt();
        try{
            if (H > 0 && B >0 )
                System.out.println(H * B);
            else
                throw new Exception("Breadth and height must be positive"
);
}
        catch (Exception e) {
            System.out.println(e);
        }
            
        
        sc.close();
    }
}
