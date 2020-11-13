package 문자열.P5622;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int res = 0;

        for (int i=0; i<s.length(); ++i) {
            res+=dial(s.charAt(i));
        }
        System.out.println(res);
    }
    static int dial(char c) {
        switch (c) {
            case "A": case "B": case "C":
                return 3;
            case "D": case "E": case "F":
                return 4;
            case "G": case "H": case "I":
                return 5;
            case "J": case "K": case "L":
                return 6;
            case "M": case "N": case "O":
                return 7;
            case "P": case "Q": case "R": case "S":
                return 8;
            case "T": case "U": case "V":
                return 9;
            case "W": case "X": case "Y": case "Z":
                return 10;
        }
    }
}
