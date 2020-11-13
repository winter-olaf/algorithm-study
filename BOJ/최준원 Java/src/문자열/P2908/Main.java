package 문자열.P2908;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        sc.close();
        String a = "";
        String b = "";
        for (int i=2; i>=0; --i) {
            a += str[0].charAt(i);
            b += str[1].charAt(i);
        }
        int c = Integer.parseInt(a);
        int d = Integer.parseInt(b);
        if (c > d)
            System.out.print(c);
        else
            System.out.print(d);
    }
}
