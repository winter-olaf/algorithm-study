package DAY01.sort;

import java.util.Arrays;
import java.util.Comparator;

public class SortTest {
	public static void main(String[] args) {
		System.out.println("hello");
		
		Point[] array = new Point[5];
		array[0] = new Point(0, 0, 1);
		array[1] = new Point(0, 1, 3);
		array[2] = new Point(0, 2, 4);
		array[3] = new Point(3, 0, 5);
		array[4] = new Point(4, 0, 2);
		
		System.out.println(Arrays.toString(array));
		
		// 특별한 조건의 정렬 속성
		Arrays.sort(array, new Comparator<Point>() {
			@Override
			public int compare(Point arg0, Point arg1) {
				if (arg0.y < arg1.y) { // -1 : 데이터를 바꾸지 않음 => 우리가 원하는 순서
					return -1;
				} else if (arg0.y == arg1.y) { // 0 : 같음
					return 0;
				} else { // 1: 데이터를 바꿈 => 우리가 원하는 순서가 아님
					return 1;
				}
			}
		});
		System.out.println(Arrays.toString(array));
		
		// 컴패러터를 지정한 뒤의 정렬
		Arrays.sort(array);
		System.out.println(Arrays.toString(array));
	}
}
// 기본 정렬 속성
class Point implements Comparable<Point> {
	int y;
	int x;
	int value;
	
	public Point(int y, int x, int value) {
		super();
		this.y = y;
		this.x = x;
		this.value = value;
	}
	
	@Override
	public String toString() {
		return "[x=" + x + ", y=" + y + ", value =" + value + "]";
	}
	
	@Override
	public int compareTo(Point arg0) {
		if (x > arg0.x) {
			return -1;
		} else if () {
			
		} else {
			
		}
	}
}
