import java.util.*;

public class Java_1D_array {

    public static void main(String[] args) {
	   
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        
        int [] a = new int[n];
        for (int i = 0; i < n; i ++){
            int b = scan.nextInt();
            a[i] = b;
        }

    
        scan.close();

        // Prints each sequential element in array a
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}
