package kakao.p2020.p2;


import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(5)));
    }

    public static int[] solution(int n) {
        int[] answer = {};

        int[][] board = new int[n + 1][n + 1];
        int size = 0;

        for (int i = n; i > 0; i--) {
            size += i;
        }

        initBoard(1, n, 0, 0, board);

        answer = new int[size];
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <  board[i].length; j++) {
                if (board[i][j] == 0) {
                    continue;
                }
                answer[index++] = board[i][j];
            }
        }

        return answer;
    }

    public static void initBoard(int startValue, int n, int i, int j, int[][] board) {

        if (n <= 0) {
            return;
        } else  {
            int tempValue = startValue;
            for (int t = 0; t < n; t++) {
                board[i + t][j] = tempValue++;
            }

            for (int t = 1; t < n; t++) {
                board[i + n - 1][j + t] = tempValue++;
            }

            for (int t = 1; t < n - 1; t++) {
                board[i + n - 1 - t][j + n - 1] = tempValue++;
            }

            initBoard(tempValue, n - 3, i + 2, j + 1, board);
        }
    }
}