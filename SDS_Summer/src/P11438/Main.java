package P11438;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;
    private static ArrayList<Integer>[] graph;
    private static int[][] parent;
    private static int[] depth;
    private static boolean[] visited;

    public static void main(String args[]) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        depth = new int[N + 1];
        graph = new ArrayList[N + 1];
        parent = new int[N + 1][17];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        // graph modeling
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            graph[from].add(to);
            graph[to].add(from);
        }

        // tree making
        dfs(0, 1, 1);

        // parentfill
        for (int k = 1; k < 17; k++) {
            for (int i = 1; i <= N; i++) {
                parent[i][k] = parent[parent[i][k - 1]][k - 1];
            }
        }

        // lca query
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int lca = lca(a, b);
            bw.write(lca + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    private static int lca(int a, int b) {
        // 1. a가 b보다 깊지 않으면 자리를 바꾼다.
        if (depth[a] < depth[b]) {
            int temp = a;
            a = b;
            b = temp;
        }

        // 2. a와 b의 깊이를 같게 맞춘다.
        for (int i = 16; i >= 0; i--) {
            if (depth[parent[a][i]] >= depth[b]) {
                a = parent[a][i];
            }
        }

        // 3. a 와 b 가 같으면 그냥 return 한다.
        // a와 b는 동일 경로 위에 위치하고 있기 때문이다.
        if (a == b) {
            return a;
        }

        // 4. 공통 조상이 같기 전까지 올려보낸다.
        // 이 때 i 는 큰 것부터 작은 것으로 내려가야 한다는 점에 주의한다.
        for (int i = 16; i >= 0; i--) {
            if (parent[a][i] != parent[b][i]) {
                a = parent[a][i];
                b = parent[b][i];
            }
        }

        // 5. 바로 위의 것을 올린다.(이 때는 a로 해도 되고 b로 해도 상관없다)
        return parent[a][0];
    }

    private static void dfs(int prev, int now, int d) {
        depth[now] = d;
        parent[now][0] = prev;

        for (int i = 0; i < graph[now].size(); i++) {
            int next = graph[now].get(i);
            if (next == prev)
                continue;
            if (depth[next] == 0)
                dfs(now, next, d + 1);
        }
    }

}