package P4344;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        for (int i=0; i<n; i++) {
            int k = sc.nextInt();
            double total = 0;
            double avg = 0;
            int idx = 0;
            int[] score = new int[k];
            for (int j = 0; j < k; j++) {
                total+=sc.nextInt();
                score[idx] = sc.nextInt();
                idx++;
            }
            avg = total / k;
            idx = 0;
            double result = 0;
            for (int j = 0; j < k; j++) {
                if (avg < score[idx]) {
                    result++;
                }
                idx++;
            }
            double res = k/result;
            System.out.printf(String.format("%.3f", res));
        }
    }
}
