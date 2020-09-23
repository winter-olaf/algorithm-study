# 5-10
n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]

def dfs(x,y):
    # 주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 노드도 재귀적으로 방문 처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    # 그 외는 False
    return False

result = 0
# 모든 노드에 대해 음료수 채우기
for i in range(n):
    for j in range(m):
        print(graph)
        if dfs(i,j) == True:
            result += 1
print(result)
'''
4 5
00110
00011
11111
00000
'''
