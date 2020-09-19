package P11051;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class Main {

    static int[][] dp;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        dp = new int[N + 1][N + 1];

        for(int n = 1; n <= N; n++) {
            for (int k = 0; k <= n; k++) {
                if(n == k || k == 0) {
                    dp[n][k] = 1;
                }else {
                    dp[n][k] = (dp[n - 1][k - 1] + dp[n - 1][k]) % 10007;
                }
            }
        }

        System.out.println(dp[N][K]);
    }
}