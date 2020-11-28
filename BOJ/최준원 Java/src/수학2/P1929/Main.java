package 수학2.P1929;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int a = s.nextInt();
        int b = s.nextInt();
        for (int i=a; i<=b; ++i) {
            if (isPrime(i) == 0) {
                System.out.println(i);
            }
        }
    }
    static int isPrime(int n) {
        if (n < 2)
            return 1;
        int i = 2;
        while (i <= n / i) {
            if (n%i == 0)
                return 1;
            ++i;
        }
        return 0;
    }
}
