#include <iostream>
#include <queue>

using namespace std;

int mat[1001][1001];
int chk[1001];
int N, M;
int connect_count = 1;


void dfs(int node) {
    chk[node] = 1;
    for (int i = 1; i <= N; i++) {
        if (mat[node][i] != 0 && chk[i] == 0) {
            dfs(i);
        }
    }
}


int main()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        mat[u][v] = 1;
        mat[v][u] = 1;

    }

    dfs(1);

    while (true) {
        bool isCheckAll = true;
        for (int i = 1; i <= N; i++) {
            if (chk[i] == 0) {
                dfs(i);
                isCheckAll = false;
                break;
            }
        }
        if (isCheckAll) {
            cout << connect_count << endl;
            return 0;
        }
        connect_count += 1;
    }

}