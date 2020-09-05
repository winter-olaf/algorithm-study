package SCPC다이어트;

import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

import java.util.Scanner;

/*
   As the name of the class should be Solution , using Solution.java as the filename is recommended.
   In any case, you can execute your program by running 'java Solution' command.
 */
class Solution {
	static int Answer;

	public static void main(String args[]) throws Exception	{
		/*
		   The method below means that the program will read from input.txt, instead of standard(keyboard) input.
		   To test your program, you may save input data in input.txt file,
		   and call below method to read from the file when using nextInt() method.
		   You may remove the comment symbols(//) in the below statement and use it.
		   But before submission, you must remove the freopen function or rewrite comment symbols(//).
		 */		

		/*
		   Make new scanner from standard input System.in, and read data.
		 */
		Scanner sc = new Scanner(new FileInputStream("src\\SCPC다이어트\\sample_input.txt"));
// 		Scanner sc = new Scanner(System.in);
		

		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {

			Answer = 0;
			
			int N = sc.nextInt();
			int K = sc.nextInt();
			
			int[] A = new int[N];
			int[] B = new int[N];
			
			
			
			ArrayList<Integer> tmp = new ArrayList<Integer>();
			int[][] resultArr;
			
			for (int i=0; i<N; i++) {
				A[i] = sc.nextInt();
			}
			for (int i=0; i<N; i++) {
				B[i] = sc.nextInt();
			}
			for (int i=0; i<N; i++) {
				for (int j=0; j<N; j++) {
					tmp.add(A[i] + B[j]);
				}
			}
			System.out.println(tmp);
			
//			for (int ii : tmp) {
//				System.out.println(ii);
//			}
			// Print the answer to standard output(screen).
//			System.out.println("Case #"+(test_case+1));
//			System.out.println(Answer);
		}
	}
}