V = 7 # 노드의 수
E = 8 # 간선의 수
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7] # 간선 정보

# 인접 행렬 초기화 : 노드 간의 연결관계를 표시하는 2차원 배열
adj = [[0]*(V+1) for x in range(V+1)]

# 인접 행렬에 노드 정보 넣기
for i in range(0, E*2, 2):
    s = edges[i]
    e = edges[i + 1]
    adj[s][e] = 1
    adj[e][s] = 1

def bfs(v):
    # BFS는 먼저 방문한 노드가 먼저 버려지므로 queue를 사용한다.
    queue = [v]
    visited = [False] * (V+1)
    visited[v] = True

    while queue:
        front = queue.pop()
        # queue에서 가장앞에 있는 정점을 방문
        print(front, end=" ")

        # 해당 정점에서 방문할 수 있는 모든 경로를 queue에 차곡차곡 넣어준다
        for i in range(1, V+1):
            if adj[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(1)