V, E, S = map(int, input().split())
edges = [list(map(int, input().split())) for x in range(E)]
adj = [[0]*(V+1) for x in range(V+1)]

# Connect Graph
for i in edges:
    a = i[0]
    b = i[1]
    adj[a][b] = 1
    adj[b][a] = 1

dfs_visited = [0] * (V + 1)
def dfs(v):
    dfs_visited[v] = 1
    print(v, end=" ")
    for i in range(1, V+1):
        if adj[v][i] and not dfs_visited[i]:
            dfs(i)

def bfs(v):
    visited = [0] * (V+1)
    visited[v] = 1
    queue = [v]

    while queue:
        top = queue.pop(0)
        print(top, end=" ")
        for i in range(1, V+1):
            if adj[top][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
dres = dfs(S)
print()
bres = bfs(S)
