#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;
#define MAXN 100001

int N, M;
vector<int> graph[MAXN];
int parent[MAXN][17];
int depth[MAXN];

int lca(int a, int b) {
    //1. a가 b보다 깊지 않으면 자리를 바꾼다.
    if (depth[a] < depth[b]) {
        int temp = a;
        a = b;
        b = temp;
    }

    //2. a와 b의 깊이를 같게 맞춘다.
    for (int i = 16; i >= 0; i--) {
        if (depth[parent[a][i]] >= depth[b]) {
            a = parent[a][i];
        }
    }

    //3. a 와 b 가 같으면 그냥 return 한다.
    // a와 b는 동일 경로 위에 위치하고 있기 때문이다.
    if (a == b) {
        return a;
    }

    //4. 공통 조상이 같기 전까지 올려보낸다.
    // 이 때 i 는 큰 것부터 작은 것으로 내려가야 한다는 점에 주의한다.
    for (int i = 16; i >= 0; i--) {
        if (parent[a][i] != parent[b][i]) {
            a = parent[a][i];
            b = parent[b][i];
        }
    }

    //5. 바로 위의 것을 올린다.(이 때는 a로 해도 되고 b로 해도 상관없다)
    return parent[a][0];
}

int main() {

    ios_base::sync_with_stdio(0); 
    cin.tie(0); 
    cout.tie(0);

    //graph modeling
    cin >> N;
    for (int i = 0; i < N - 1; i++) {
        int from, to;
        cin >> from >> to;
        graph[from].push_back(to);
        graph[to].push_back(from);
    }

    //tree making
    queue<int> q;
    int root = 1;
    q.push(root);
    depth[root] = 1;
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        for (int i = 0; i < graph[now].size(); i++) {
            int next = graph[now][i];
            if (depth[next] == 0) {
                depth[next] = depth[now] + 1;
                q.push(next);
                parent[next][0] = now;
            }
        }
    }

    // parentfill
    for (int k = 1; k < 17; k++) {
        for (int i = 1; i <= N; i++) {
            parent[i][k] = parent[parent[i][k - 1]][k - 1];
        }
    }

    //lca query
    cin >> M;
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        cout << lca(a, b) << "\n";
    }

    return 0;
}