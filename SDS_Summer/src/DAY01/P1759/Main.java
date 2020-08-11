package DAY01.P1759;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int L;
	static int C;
	static char[] data;
	static StringBuilder sb;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		System.setIn(new FileInputStream("src\\DAY01\\P1759\\input.txt"));
		Scanner sc = new Scanner(System.in);
		
		L = sc.nextInt();
		C = sc.nextInt();
		
		data = new char[C];
		
		for (int i=0; i<C; i++) {
			data[i] = sc.next().charAt(0);
		}
		Arrays.sort(data);
		/*
		for (int i = 0; i < C; i++) {
			if (data[i] == 'a' || data[i] == 'e' || data[i] == 'i' || data[i] == 'o' || data[i] == 'u') {
				dfs(1, 0, 1, i, data[i] + "");
			} else {
				dfs(1, 1, 0, i, data[i] + "");
			}
		}*/
		// 임의의 시작점을 만듦으로써 코드를 대폭 줄일 수 있다.
		dfs(0,0,0,-1,null);
		
	}
//	static StringBuilder dfs(int length, int con, int vow, int current, String pwd) {
	static void dfs(int length, int con, int vow, int current, String pwd) {
//		1.체크인 - 생략 가능
//		2.목적지인가?
		if (length==L) {
			if (con >= 2 && vow >= 1) {
				// 답 발견. 출력 or 저장
				System.out.println(pwd);
			}
		} else {
//		3.갈 수 있는 곳을 순회	
		} for (int i = current + 1; i < C; i++) {
//			4.갈 수 있는가? - 생략 가능
//			5.간다. dfs(next)
			if (data[i] == 'a' || data[i] == 'e' || data[i] == 'i' || data[i] == 'o' || data[i] == 'u') {
				dfs(length + 1, con, vow + 1, i, pwd + data[i]);
			} else {
				dfs(length + 1, con + 1, vow, i, pwd + data[i]);
			}
		}
//		6.체크아웃 - 생략 가능
	}

}
