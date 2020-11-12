package 함수.P4673;

public class Main {
    public static int isSelf(int i) {
        int res = i;
        while (i > 0) {
            res+=i%10;
            i/=10;
        }
        return (res);
    }
    public static void main(String[] args) {
        boolean[] res = new boolean[10001];

        for (int i=1; i<10001; ++i) {
            int n = isSelf(i);
            if (n <= 10000) {
                res[n] = true;
            }
        }

        for (int i=1; i<10001; ++i) {
            if (!res[i]) {
                System.out.println(i);
            }
        }
    }
}
//public class Main {
//    public static void main(String[] args) {
//        boolean[] ans = new boolean[10001];
//        int a, b, c, d, e, res;
//        for (int i=1; i<10001; ++i) {
//            a = i/10000;
//            b = i/1000;
//            c = (i/100)%10;
//            d = (i/10)%10;
//            e = i%10;
//            res = i + (a+b+c+d+e);
//            if (res <= 10000) {
//                ans[res] = true;
//            }
//        }
//
//        for (int i=1; i<10001; ++i) {
//            if (!ans[i]) {
//                System.out.println(i);
//            }
//        }
//    }
//}
