# 메모리 초과 해결은 인접 리스트로
from sys import stdin

def dfs(v):
    stack = [v]
    visited[v] = 7 # 칠해야되니까 7... 시작점을 칠하고 출발

    while stack:
        top = stack.pop()
        # 인접 리스트에서
        for i in adj[top]:
            if not visited[i]:
                stack.append(i)
                visited[i] = visited[top] * -1
            elif visited[i] == visited[top]:
                return False
    return True

K = int(stdin.readline())

for tc in range(K):
    V, E = map(int, stdin.readline().split())
    edges = [list(map(int, stdin.readline().split())) for x in range(E)]
    # 이 문제를 인접 행렬로 풀려고 했기 때문에 에러가 난 것. 인접 리스트로 바꿔 보자.
    # adj = [[0]*(V+1) for x in range(V+1)]
    adj = [[] for x in range(V+1)]
    # visited: 방문 체크 겸 색깔 체크 리스트
    visited = [0] * (V + 1)
    res = 'YES'

    for i,j in edges:
        adj[i].append(j)
        adj[j].append(i)

    # 1에서만 DFS 하는게 아니라 모든 정점에서 DFS를 해줘야 한다.
    for i in range(1, V+1):
        if not visited[i]: # 아직 방문하지 않았다면
            if not dfs(i):
                res = 'NO'
                break
    print(res)


'''
반례
1
5 4
1 2
1 3
2 3
4 5

2
4 4
1 2
2 3
3 4
4 1
4 4
1 2
2 3
3 4
4 2
YES
NO

둘 다 0일 때 임의로 홀수번과 짝수번을 정해줘서는 답을 찾을 수 없다
2
4 3
1 2
4 3
2 3
4 4
2 3
1 4
3 4
1 2
'''
