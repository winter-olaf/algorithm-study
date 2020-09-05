package P13251;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int M, K;
    static int[] nums;
    static int sum;
    static double result;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        M = Integer.parseInt(br.readLine());

        nums = new int[M];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            sum += nums[i];
        }
        K = Integer.parseInt(br.readLine());
//      System.out.println(Arrays.toString(nums));
//      System.out.println(sum);
        for (int i = 0; i < M; i++) {
            double temp = 1;
            double colorCount = nums[i];
            double totalCount = sum;
            for (int k = 0; k < K; k++) {
                temp *= colorCount-- / totalCount--;
            }
            result += temp;
        }
        System.out.println(result);
    }

}