package 수학2.P2581;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int sum, min;
        sum = 0;
        min = 0;

        int a = s.nextInt();
        s.nextLine();
        int b = s.nextInt();
        for (int i=a; i<=b; ++i) {
            if (isPrime(i) == 0) {
                if (min == 0)
                    min = i;
                sum+=i;
            }
        }
        if (sum == 0)
            System.out.println(-1);
        else {
            System.out.println(sum);
            System.out.println(min);
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
