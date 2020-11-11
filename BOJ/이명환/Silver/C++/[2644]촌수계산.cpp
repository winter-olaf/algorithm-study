//#include <queue>
//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//vector < vector <int> > family(101);
//bool chk[101];
//int x, y;
//vector <int> count_list(101);
//
//int dfs(int node, int count) {
//    chk[node] = true;
//    if (node == y) return count;
//    for (int i = 0; i < family[node].size(); i++) {
//        if (chk[family[node][i]] == false) {
//            return dfs(family[node][i], count + 1);
//        }
//    }
//    return 0;
//}
//
//int main() {
//    int N; cin >> N;
//    cin >> x >> y;
//    int V; cin >> V;
//
//
//    for (int i = 0; i < V; i++) {
//        int f, l; cin >> f >> l;
//        family[f].push_back(l);
//        family[l].push_back(f);
//    }
//
//    int ans = dfs(x,0);
//   
//
//    if (ans == 0) cout << "-1" << endl;
//    else cout << ans << endl;
//
//}

#include<iostream>
#include<queue>
using namespace std;

queue<int> q;

int N, M;
int desx, desy;
int map[101][101];
int visited[101];

void BFS() {
    int i;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (i = 1; i <= N; i++) {
            if (map[cur][i] == 1 && visited[i] == 0) {
                visited[i] = visited[cur] + 1;
                q.push(i);
            }
        }
    }
}

int main()
{
    cin >> N;
    cin >> desx >> desy;
    cin >> M;

    int i, j;
    int x, y;
    for (i = 0; i < M; i++) {
        cin >> x >> y;
        map[x][y] = map[y][x] = 1;
    }

    visited[desx] = 1;
    q.push(desx);
    BFS();
    cout << visited[desy] - 1;
    return 0;
}