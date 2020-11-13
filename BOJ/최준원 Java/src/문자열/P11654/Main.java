package 문자열.P11654;

import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
//        Scanner sc = new Scanner(System.in);
//        char a = sc.nextLine().charAt(0);
//        int res = (int)a;
//        System.out.println(res);
        // 1Byte만 읽어도 되는 경우이므로 기본 InputStream으로 읽으면 효율적이다.
        int a = System.in.read();
        System.out.println(a);
    }
}
