package 수학1.P1011;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i<t; ++i) {
            String[] tc = br.readLine().split(" ");
            int a = Integer.parseInt(tc[0]);
            int b = Integer.parseInt(tc[1]);
            int distance = b - a;
            int max = (int)Math.sqrt(distance);

            if (max == Math.sqrt(distance))
                System.out.println(max * 2 - 1);
            else if (distance <= max * max + max)
                System.out.println(2 * max);
            else
                System.out.println(2 * max + 1);
        }
    }
}
