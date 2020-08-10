package DAY01.P3055;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int R, C;
	static char[][] map;
	static Queue<Point> queue;
	static boolean foundAnswer;
	static List<Point> waterList = new ArrayList<>(); 
	static int[] my;
	static int[] mx;
	static int [][] dp;
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("src\\DAY01\\P3055\\input.txt"));
		
		Scanner sc = new Scanner(System.in);
		
		R = sc.nextInt();
		C = sc.nextInt();
		
		map = new char[R][C];
		dp = new int[R][C];
		queue = new LinkedList<>();
		
		for (int r=0; r < R; r++) {
			String line = sc.next();
			for (int c = 0; c < C; c++) {
				map[r][c] = line.charAt(c);
				if (map[r][c] == 'S') {
					queue.add(new Point(r, c, 'S'));
				} else if (map[r][c] == '*' ) {
					queue.add(new Point(r, c, '*')); // waterList에 임시로 물 저장
				}
			}
		}
		queue.addAll(waterList);
		
		for (int r=0; r < R; r++) {
			System.out.println(Arrays.toString(map[r]));
		}
		
//		Point p = new Point(0, 0, '*');
		while (!queue.isEmpty()) {
//			1. 큐에서 꺼내옴
			Point p = queue.poll();
//			2. 목적지인가?
			if (p.type == 'D') {
				// 목적지 도착
				System.out.println(dp[p.y][p.x]);
				foundAnswer = true;
				break;
			}
			// 큐에 넣을때  고슴도치 위치를 물보다 먼저 넣는 이유?
			// 고슴도치를 먼저 이동시키고 물이 이동할 곳은 자연스럽게 '*'로 덮어지게 한 코드
			
//			3. 갈수 있는 곳을 순회(좌,우,위,아래)
			for (int i=0; i<4; i++) {
				int ty = p.y +my[i];
				int tx = p.x +mx[i];
//				4. 갈수 있는가? if (맵을 벗어나지 않고, X가 아니고, * 아니고)
					if (0 <= ty && ty < R && 0 <= tx && tx < C) {
						if (p.type == '.' || p.type == 'S') {
							if (dp[ty][tx] == 0 && checkSafe(ty, tx)) {
//								5. 체크인 dp[r][c] = time
								dp[ty][tx] = dp[p.y][p.x] + 1;
//								6. 큐에 넣음 queue.add(next)
								queue.add(new Point(ty, tx, map[ty][tx]));
							}
						}
					} else if (p.type == '*' && map[ty][tx] == '.') { //물에 대한 동작
//						6. 큐에 넣음 queue.add(next)
						queue.add(new Point(ty, tx, '*'));
						map[ty][tx] = '*';
					}
			}
		}
		if (foundAnswer == false) {
			System.out.println("KAKTUS");
		}
	}
// X가 아니고 * 아니고, *에 인접한 .도 아님을 체크
	static boolean checkSafe(int y, int x) {
		if (map[y][x] == 'D') {
			return true;
		} else if (map[y][x] == '.') {
			for (int i=0; i<4; i++) {
				int ty = y + my[i];
				int tx = x + mx[i];
				if (0 <= ty && ty < R && 0 <= tx && tx < C && map[ty][tx] == '*') {
					return false;
				}
			}
			return true;
		} else {
			return false;
		}
	}
}

class Point {
	int y;
	int x;
	char type;
	
	public Point(int y, int x, char type) {
		super();
		this.y = y;
		this.x = x;
		this.type = type;
	}
	
}
