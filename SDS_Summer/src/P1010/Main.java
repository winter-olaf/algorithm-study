package P1010;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class Main {

    static int T, N, M;

    static int[][] dp = new int[31][31];
    static int count;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(System.in);

        for (int n = 0; n <= 30; n++) {
            for (int k = 0; k <= n; k++) {
                if (n == k || k == 0) {
                    dp[n][k] = 1;
                } else {
                    dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k];
                }
            }
        }

        T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            N = sc.nextInt();
            M = sc.nextInt();

            System.out.println(dp[M][N]);
        }

    }
}