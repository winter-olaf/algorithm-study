package 수학2.P1002;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        int a,b,c,d,e,f;
        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            String[] l = br.readLine().split(" ");
            a = Integer.parseInt(l[0]);
            b = Integer.parseInt(l[1]);
            c = Integer.parseInt(l[2]);
            d = Integer.parseInt(l[3]);
            e = Integer.parseInt(l[4]);
            f = Integer.parseInt(l[5]);

            sb.append(turret(a,b,c,d,e,f)).append('\n');
        }
        System.out.println(sb);
    }

    static int turret(int x1, int y1, int r1, int x2, int y2, int r2) {
        int distance_pow = (int)(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));

        if (x1==x2 && y1==y2 && r1==r2)
            return -1;
        else if (distance_pow > Math.pow(r1 + r2, 2))
            return 0;
        else if (distance_pow < Math.pow(r1 - r2, 2))
            return 0;
        else if (distance_pow == Math.pow(r1 - r2, 2))
            return 1;
        else if (distance_pow == Math.pow(r1 + r2, 2))
            return 1;
        else
            return 2;
    }
}
