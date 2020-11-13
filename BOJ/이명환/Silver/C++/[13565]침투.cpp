#include <iostream>
#include <queue>

using namespace std;

int mat[1001][1001];
int chk[1001][1001];
int M, N;
int dir[4][2] = { {1,0},{-1,0},{0,1},{0,-1} };


void dfs(int y, int x) {
    chk[y][x] = 1;
    for (int i = 0; i < 4; i++) {
        int yy = y + dir[i][0], xx = x + dir[i][1];
        if (yy < 0 || yy >= M || xx < 0 || x >= N) continue;
        if (mat[yy][xx] == 0 && chk[yy][xx] == 0) {
            dfs(yy, xx);
        }
    }

}


int main()
{
    cin >> M >> N;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            scanf_s("%1d", &mat[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        if (mat[0][i] == 0) {
            dfs(0, i);
        }
    }

    for (int i = 0; i < N; i++) {
        if (chk[M-1][i] == 1) {
            cout << "YES" << endl;
            return 0;
        }
    }
    cout << "NO" << endl;
}