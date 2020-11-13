package 문자열.P2675;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        for (int i=0; i<n; ++i) {
//            int r = sc.nextInt();
//            String s = sc.next(); // nextLine으로 읽으면 공백까지 출력하기 때문에 안된다.
//            for (int j=0; j<s.length(); ++j) {
//                for (int k=0; k<r; ++k) {
//                    System.out.print(s.charAt(j));
//                }
//            }
//            System.out.println();
//        }
        // Using StringBuilder to avoid using multiple OutputStream
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; ++i) {
            String[] str = br.readLine().split(" ");
            int r = Integer.parseInt(str[0]);
            String s = str[1];

            for (int j=0; j<s.length(); ++j) {
                for (int k=0; k<r; ++k) {
                    sb.append(s.charAt(j));
                }
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}
