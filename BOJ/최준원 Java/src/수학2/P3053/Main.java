package 수학2.P3053;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int R = sc.nextInt();
        System.out.printf("%.6f\n", R*R*Math.PI);
        // float로 하니까 틀렸었음
        System.out.printf("%.6f", (double)R*R*2);
    }
}
