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

def dfs(v):
    # DFS는 마지막에 방문한 노드가 먼저 버려지므로 스택을 사용한다.
    stack = [v]

    # 방문 여부를 체크하기 위한 배열
    visited = [False] * (V+1)
    # v부터 시작하므로 방문했음을 체크
    visited[v] = True
    # 시작점을 출력하기 위해 이곳에서 출력
    print(v, end=" ")

    while stack:
        # 스택의 맨 위를 바로 빼버린다. (맨 마지막 원소)
        # 반복문을 순회하면서 돌 곳이 없으면 한 단계씩 pop하며 스택의 크기가 줄어들고,
        # 스택의 길이가 0이 되면 반복문이 종료된다.
        top = stack[-1]

        # 해당 노드에서 갈 수 있는 경로가 있는지 탐색
        for i in range(1, V+1):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = True
                print(i, end=" ")
                break
        # for문을 전체 돌았는데도 갈 수 있는 경로가 없을 경우 pop
        else:
            stack.pop()

# pop을 먼저 해버리는 dfs
# 탐색 순서는 조금 다르지만 완전 탐색을 한다는 점에서는 dfs이다.
def dfs2(v):
    stack = [v]
    visited = [False] * (V+1)

    visited[v] = True

    # 위 방법이랑 다른 점은, 한 정점에 방문하면 해당 정점에서 방문할 수 있는 모든 정점을 스택에 넣어준다는 것.
    # 해당 정점은 재방문할 필요가 없다.
    # 숫자가 큰 노드부터 방문하게 된다.
    while stack:
        # 그때그때 빼버림
        top = stack.pop()
        print(top, end=" ")
        # top에서 갈 수 있는 모든 정점을 스택에 넣는다
        for i in range(1, V+1):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = True

# 함수를 재귀적으로 참조하기 때문에 외부에 visited 배열을 선언해 둔다.
recursive_visited = [0] * (V+1)

def recursive_dfs(v):
    # 현재 정점을 1로 변경
    recursive_visited[v] = 1
    print(v, end=" ")

    for i in range(1, V+1):
        if adj[v][i] and not recursive_visited[i]:
            recursive_dfs(i)

dfs(1)
print()
dfs2(1)
print()
recursive_dfs(1)

1 2 4 6 5 7 3
1 3 7 6 5 4 2
1 2 4 6 5 7 3