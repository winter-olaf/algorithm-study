package 수학2.P3009;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> A = new ArrayList<String>();
        ArrayList<String> B = new ArrayList<String>();

        for (int i=0; i<3; ++i) {
            String[] tmp = br.readLine().split(" ");
            String a = tmp[0];
            String b = tmp[1];

            if (A.indexOf(a) == -1)
                A.add(a);
            else
                A.remove(A.indexOf(a));
            if (B.indexOf(b) == -1)
                B.add(b);
            else
                B.remove(B.indexOf(b));
        }
        System.out.printf("%s %s", A.get(0), B.get(0));
    }
}
