import java.io.*;
import java.util.*;

public class Subarray {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        
        int count = 0;
        int N = input.nextInt();    // Getting total no of elements
        int [] Array = new int[N];
        
        // Creating an array
        for (int i = 0; i < N; i ++){
            
            int a = input.nextInt();        // Getting elements
            Array[i] = a;
        }
        input.close();
        
        // Logic
        
        for (int i = 0; i < N; i++){
            int sum = 0;
            
            for (int j = i; j < N; j++ ){
                sum += Array[j]; 
                
                if (sum < 0) count += 1;
    
            }
        }
        
        System.out.println(count);
        
        
    }
}

// T : O(n^2)      S: O(n)
