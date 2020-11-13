package 함수.P1065;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int res, a, b, c;
        res = 0;
        int n = sc.nextInt();
        for (int i=1; i<=n; ++i) {
            if (i <= 99)
                res++;
//            else if (i == 1000) 해줄 필요 없음. 왜 했던거지?
//                break;
            else {
                a = i/100;
                b = (i/10)%10;
                c = i%10;
                if ((a - b) == (b - c))
                    res++;
            }
        }
        System.out.println(res);
    }
}
