V = int(input())
E = int(input())

edges = [list(map(int, input().split())) for x in range(E)]
adj = [[0]*(V+1) for x in range(V+1)]

for a,b in edges:
    adj[a][b] = 1
    adj[b][a] = 1

visited = [False] * (V+1)
res = 0

def dfs(v):
    global res
    visited[v] = True
    res += 1
    for i in range(1, V+1):
        if adj[v][i] and not visited[i]:
            dfs(i)

dfs(1)
print(res-1) # 시작점 제외