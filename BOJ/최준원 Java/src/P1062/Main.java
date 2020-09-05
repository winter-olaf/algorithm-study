package P1062;

import java.io.FileInputStream;
import java.util.*;

public class Main {
	
	static int N, K;
	static String[] words;
	static boolean[] studied;
	static int studiedCount = 0;
	static int result = 0;
	static int test = 0;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		System.setIn(new FileInputStream("src\\P1062\\input.txt"));
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		K = sc.nextInt();
		
//		System.out.println(N + ", " + K);
		
		words = new String[N];
		
		for (int i=0; i<N; i++) {
			// antic은 생각할 필요가 없으므로 삭제
			words[i] = sc.next().replaceAll("[antic]", "");
		}
		
		studied = new boolean[26]; // 알파벳 전체에 해당하는 배열 생성
		studied['a' - 'a'] = true; // antic 은 배웠으므로 true로 체크
		studied['n' - 'a'] = true;
		studied['t' - 'a'] = true;
		studied['i' - 'a'] = true;
		studied['c' - 'a'] = true;
		
		// 배울 수 있는 글자가 5보다 작다면 당연히 결과는 0
		if (K<5) {
			System.out.println(0);
			return;
		// 배울 수 있는 글자가 26개라면 모든 단어 학습이 가능
		} else if (K==26) {
			System.out.println(N);
			return;
		}
		
		// 학습한 문자에 기본적으로 antic 5글자는 들어가 있음
		studiedCount = 5;
		// 일차적으로 결과를 뽑는다. 
		result = studyWords();
		// #단어 탐색 1
		for (int i=0; i<26; i++) {
			if (studied[i] == false) {
				dfs(i);
			}
		}
		System.out.println(result);
	}
	
	static void dfs(int index) {
		studied[index] = true; // 아직 공부하지 않은 글자에 한해서 dfs를 돌린다.
		studiedCount++;
		if (studiedCount == K) { // 공부 끝!
			result = Math.max(studyWords(), result);
		} else {
			// #단어 탐색 2
			for (int i=index+1; i<26; i++) {
				if (studied[i] == false) {
					dfs(i);
				}
			}
		}
		studied[index] = false; 
		studiedCount--;
		
	}
	
	static int studyWords() {
		int count = 0;
		for (int i=0; i<N; i++) {
			boolean isIn = true;
			String word = words[i];
			for (int j=0; j<word.length(); j++) {
				// 단어 중, 한 글자라도 배운적이 없으면 그 단어는 꽝
				if (studied[word.charAt(j) - 'a'] == false) {
					isIn = false;
					break;
				}
			}
			if (isIn == true) {
				count++;
			}
		}
		return count;
	}

}
