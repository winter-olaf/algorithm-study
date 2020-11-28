package 수학2.P4948;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n, res;

        while (true) {
            n = Integer.parseInt(br.readLine());
            if (n == 0)
                break;
            res = 0;
            for (int i=n+1; i<=n*2; ++i) {
                if (isPrime(i) == 0)
                    res++;
            }
            System.out.println(res);
        }
    }
    ;
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
