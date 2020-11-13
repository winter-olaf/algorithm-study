package 문자열.P1157;

import java.util.Scanner;

public class Main {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        String s = sc.next();
//        int[] res = new int[26];
//        for (int i=0; i<s.length(); ++i) {
//            char c = s.charAt(i);
//            if (c >= 'a' && c <= 'z')
//                res[c - 'a']++;
//            else if (c >= 'A' && c <= 'Z')
//                res[c - 'A']++;
//        }
//        int max = 0;
//        char result = '?';
//        for (int i=0; i<26; ++i) {
//            if (max < res[i]) {
//                max = res[i];
//                result = (char)(i + 65);
//            }
//            else if (max == res[i])
//                result = '?';
//        }
//        System.out.print(result);
//    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next().toUpperCase();

        int[] res = new int[26];
        int max = 0;
        char result = '?';

        for (int i=0; i<str.length(); ++i) {
            res[str.charAt(i) - 65]++;
            if (max < res[str.charAt(i) - 65]) {
                max = res[str.charAt(i) - 65];
                result = str.charAt(i);
            }
            else if (max == res[str.charAt(i) - 65]) {
                result = '?';
            }
        }
        System.out.print(result);
    }
}
