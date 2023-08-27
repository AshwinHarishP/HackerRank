import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Biginteger {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        String a = input.nextLine();
        String b = input.nextLine();
        
        BigInteger number_1 = new BigInteger(a);
        BigInteger number_2 = new BigInteger(b);
        
        System.out.println(number_1.add(number_2));
        System.out.println(number_1.multiply(number_2));
        
        
        
        input.close();
    }
}
