package 입출력과사칙연산.P10818;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int min = 1000001;
        int max = -1000001;
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//        int idx = 0;
//        int[] arr = new int[n];
//
//        while(st.hasMoreTokens()) {
//            arr[idx] = Integer.parseInt(st.nextToken());
//            idx++;
//        }
        // 배열을 쓰면 메모리 할당, 배열 정렬 측면에서 비효율적이다. 안 쓰는 방법은
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        br.close();
        System.out.printf("%d %d",min, max);
    }
}
