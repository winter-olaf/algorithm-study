package 수학2.P9020;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        int n, hn;

        for (int i=0; i<t; ++i) {
            n = Integer.parseInt(br.readLine());
            hn = n/2;
            while (hn >= 2) {
                if (isPrime(hn) == 0 && isPrime(n-hn) == 0) {
                    break;
                }
                hn--;
            }
            System.out.printf("%d %d\n", hn, n-hn);
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
