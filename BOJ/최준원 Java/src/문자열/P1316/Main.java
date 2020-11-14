package 문자열.P1316;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int result = 0;
        for (int i=0; i<n; ++i) {
            String s = br.readLine();
            int[] alpa = new int[26];
            for (int j=0; j<s.length(); ++j) {
                char c = s.charAt(j);
                if (alpa[c - 'a'] == 0) {
                    alpa[c - 'a'] = 1;
                }
                else if (alpa[c - 'a'] == 1) {
                    if (c != s.charAt(j - 1))
                        break;
                }
                if (j == s.length() - 1)
                    result++;
            }
        }
        System.out.println(result);
    }
}
