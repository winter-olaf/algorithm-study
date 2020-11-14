package 문자열.P2941;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] alpa = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        String s = sc.next();

        for (String s1 : alpa) {
            if (s.contains(s1)) {
                s = s.replaceAll(s1, "~");
            }
        }
        System.out.print(s.length());
    }
}
