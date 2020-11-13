package 문자열.P11720;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();

        int res = 0;
        for (byte value : br.readLine().getBytes()) {
            res += (value - '0');
        }
        System.out.println(res);
    }
}
