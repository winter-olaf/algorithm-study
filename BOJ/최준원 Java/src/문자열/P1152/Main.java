package 문자열.P1152;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().trim().split(" ");
        if (str[0].isEmpty())
            System.out.print(0);
        else
            System.out.print(str.length);
    }
}
