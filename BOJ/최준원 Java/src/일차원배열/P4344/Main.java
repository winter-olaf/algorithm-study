package 일차원배열.P4344;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int total, count;
        double avg;
        int[] score = new int[1000];
        for (int i=0; i<n; ++i) {
            int k = sc.nextInt();
            total = 0;
            for (int j = 0; j < k; j++) {
                score[j] = sc.nextInt();
                total += score[j];
            }
            avg = (double)total / k;
            count = 0;
            for (int j = 0; j < k; j++) {
                if (avg < score[j]) {
                    count++;
                }
            }
            System.out.printf("%.3f", 100.0 * count/k);
            System.out.println("%");
        }
        sc.close();
    }
}
