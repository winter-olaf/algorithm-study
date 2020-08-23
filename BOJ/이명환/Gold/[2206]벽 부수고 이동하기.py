import sys
sys.setrecursionlimit(10000000)
N,M = map(int,sys.stdin.readline().split())
roadMap = []
visited = [[0]*(M) for k in range(N)]
breakVisited = [[0]*(M) for z in range(N)]
for i in range(N):
    roadMap.append(list(map(int,input())))

# wallBraek 라는 boolean 으로 벽을 부쉈는지 아닌지 판별한다.

def move(i,j,wallBreak):
    if wallBreak:
        if i-1>=0 and roadMap[i-1][j] ==0 and (breakVisited[i-1][j] ==0 or breakVisited[i-1][j] > breakVisited[i][j] +1):
            breakVisited[i-1][j] = breakVisited[i][j] +1
            move(i-1,j,True)
        if i+1<=N-1 and roadMap[i+1][j] ==0 and (breakVisited[i+1][j] ==0 or breakVisited[i+1][j] > breakVisited[i][j] +1):
            breakVisited[i+1][j] = breakVisited[i][j] +1
            move(i+1,j,True)
        if j-1>=0 and roadMap[i][j-1] ==0 and (breakVisited[i][j-1] ==0 or breakVisited[i][j-1] > breakVisited[i][j] +1):
            breakVisited[i][j-1] = breakVisited[i][j] +1
            move(i,j-1,True)
        if j+1<=M-1 and roadMap[i][j+1] ==0 and (breakVisited[i][j+1] ==0 or breakVisited[i][j+1] > breakVisited[i][j] +1):
            breakVisited[i][j+1] = breakVisited[i][j] +1
            move(i,j+1,True)
    else:
        if i-1>=0 and roadMap[i-1][j] ==0 and (visited[i-1][j] ==0 or visited[i-1][j] > visited[i][j] +1):
            visited[i-1][j] = visited[i][j] +1
            move(i-1,j,False)
        elif i-1>=0 and roadMap[i-1][j] ==1 and (breakVisited[i-1][j] ==0 or breakVisited[i-1][j] > visited[i][j] +1):
            breakVisited[i-1][j]= visited[i][j] +1
            move(i-1,j,True)
        if i+1<=N-1 and roadMap[i+1][j] ==0 and (visited[i+1][j] ==0 or visited[i+1][j] > visited[i][j] +1):
            visited[i+1][j] = visited[i][j] +1
            move(i+1,j,False)
        elif i+1<=N-1 and roadMap[i+1][j] ==1 and (breakVisited[i+1][j] ==0 or breakVisited[i+1][j] > visited[i][j] +1):
            breakVisited[i+1][j]= visited[i][j] +1
            move(i+1,j,True)
        if j-1>=0 and roadMap[i][j-1] ==0 and (visited[i][j-1] ==0 or visited[i][j-1] > visited[i][j] +1):
            visited[i][j-1] = visited[i][j] +1
            move(i,j-1,False)
        elif j-1>=0 and roadMap[i][j-1] ==1 and (breakVisited[i][j-1] ==0 or breakVisited[i][j-1] > visited[i][j] +1):
            breakVisited[i][j-1]= visited[i][j] +1
            move(i,j-1,True)
        if j+1<=M-1 and roadMap[i][j+1] ==0 and (visited[i][j+1] ==0 or visited[i][j+1] > visited[i][j] +1):
            visited[i][j+1] = visited[i][j] +1
            move(i,j+1,False)
        elif j+1<=M-1 and roadMap[i][j+1] ==1 and (breakVisited[i][j+1] ==0 or breakVisited[i][j+1] > visited[i][j] +1):
            breakVisited[i][j+1]= visited[i][j] +1
            move(i,j+1,True)

move(0,0,False)
if N==1 and M ==1:
    print('1')
elif visited[N-1][M-1] == 0 and breakVisited[N-1][M-1] ==0:
    print('-1')
elif visited[N-1][M-1] != 0 and breakVisited[N-1][M-1] ==0:
    print(visited[N-1][M-1] +1)
elif visited[N-1][M-1] == 0 and breakVisited[N-1][M-1] !=0:
    print(breakVisited[N-1][M-1] +1)

else:
    print(min(visited[N-1][M-1],breakVisited[N-1][M-1])+1 )
#sys.setrecursionlimit(10000000)로 재귀 횟수를 늘려주니까 통과했다.. ㅜ 좋은 코드가 아닌가?

# 다른사람의 코드. bfs로 간결하게 구현하였다. 3차원 배열을 사용하면 쉽게 푸는듯..
# import sys
# from collections import deque
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# def bfs():
#     q = deque()
#     q.append([0, 0, 1])
#     visit = [[[0] * 2 for i in range(m)] for i in range(n)]
#     visit[0][0][1] = 1
#     while q:
#         a, b, w = q.popleft()
#         if a == n - 1 and b == m - 1:
#             return visit[a][b][w]
#         for i in range(4):
#             x = a + dx[i]
#             y = b + dy[i]
#             if 0 <= x < n and 0 <= y < m:
#                 if s[x][y] == 1 and w == 1:
#                     visit[x][y][0] = visit[a][b][1] + 1
#                     q.append([x, y, 0])
#                 elif s[x][y] == 0 and visit[x][y][w] == 0:
#                     visit[x][y][w] = visit[a][b][w] + 1
#                     q.append([x, y, w])
#     return -1
# n, m = map(int, input().split())
# s = []
# for i in range(n):
#     s.append(list(map(int, list(input().strip()))))
# print(bfs())

# 3차원 배열을 만드는데, visit[x][y][i]에서 i가 0이라면 벽을 한번 뚫은 상태이고,
# 1이라면 벽을 뚫을 수 있는 상태를 나타낸다.
# bfs을 돌려주는데 벽을 뚫을 수 있는 상태이고, 벽을 만난다면 벽을 뚫어주고 +1을 해준다.
# 아직 방문하지 않았고 벽이 아니라면 또한 +1을 해준다.