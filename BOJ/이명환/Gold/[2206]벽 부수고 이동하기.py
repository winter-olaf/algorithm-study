# import sys
# sys.setrecursionlimit(10000000)
# N,M = map(int,sys.stdin.readline().split())
# roadMap = []
# visited = [[0]*(M) for k in range(N)]
# breakVisited = [[0]*(M) for z in range(N)]
# direction = [-1,1]
#
# for i in range(N):
#     roadMap.append(list(map(int,input())))

# wallBraek 라는 boolean 으로 벽을 부쉈는지 아닌지 판별한다.
#
# def move(i,j,wallBreak):
#     if wallBreak:
#         if i-1>=0 and roadMap[i-1][j] ==0 and (breakVisited[i-1][j] ==0 or breakVisited[i-1][j] > breakVisited[i][j] +1):
#             breakVisited[i-1][j] = breakVisited[i][j] +1
#             move(i-1,j,True)
#         if i+1<=N-1 and roadMap[i+1][j] ==0 and (breakVisited[i+1][j] ==0 or breakVisited[i+1][j] > breakVisited[i][j] +1):
#             breakVisited[i+1][j] = breakVisited[i][j] +1
#             move(i+1,j,True)
#         if j-1>=0 and roadMap[i][j-1] ==0 and (breakVisited[i][j-1] ==0 or breakVisited[i][j-1] > breakVisited[i][j] +1):
#             breakVisited[i][j-1] = breakVisited[i][j] +1
#             move(i,j-1,True)
#         if j+1<=M-1 and roadMap[i][j+1] ==0 and (breakVisited[i][j+1] ==0 or breakVisited[i][j+1] > breakVisited[i][j] +1):
#             breakVisited[i][j+1] = breakVisited[i][j] +1
#             move(i,j+1,True)
#     else:
#         if i-1>=0 and roadMap[i-1][j] ==0 and (visited[i-1][j] ==0 or visited[i-1][j] > visited[i][j] +1):
#             visited[i-1][j] = visited[i][j] +1
#             move(i-1,j,False)
#         elif i-1>=0 and roadMap[i-1][j] ==1 and (breakVisited[i-1][j] ==0 or breakVisited[i-1][j] > visited[i][j] +1):
#             breakVisited[i-1][j]= visited[i][j] +1
#             move(i-1,j,True)
#         if i+1<=N-1 and roadMap[i+1][j] ==0 and (visited[i+1][j] ==0 or visited[i+1][j] > visited[i][j] +1):
#             visited[i+1][j] = visited[i][j] +1
#             move(i+1,j,False)
#         elif i+1<=N-1 and roadMap[i+1][j] ==1 and (breakVisited[i+1][j] ==0 or breakVisited[i+1][j] > visited[i][j] +1):
#             breakVisited[i+1][j]= visited[i][j] +1
#             move(i+1,j,True)
#         if j-1>=0 and roadMap[i][j-1] ==0 and (visited[i][j-1] ==0 or visited[i][j-1] > visited[i][j] +1):
#             visited[i][j-1] = visited[i][j] +1
#             move(i,j-1,False)
#         elif j-1>=0 and roadMap[i][j-1] ==1 and (breakVisited[i][j-1] ==0 or breakVisited[i][j-1] > visited[i][j] +1):
#             breakVisited[i][j-1]= visited[i][j] +1
#             move(i,j-1,True)
#         if j+1<=M-1 and roadMap[i][j+1] ==0 and (visited[i][j+1] ==0 or visited[i][j+1] > visited[i][j] +1):
#             visited[i][j+1] = visited[i][j] +1
#             move(i,j+1,False)
#         elif j+1<=M-1 and roadMap[i][j+1] ==1 and (breakVisited[i][j+1] ==0 or breakVisited[i][j+1] > visited[i][j] +1):
#             breakVisited[i][j+1]= visited[i][j] +1
#             move(i,j+1,True)
#
# move(0,0,False)
# if N==1 and M ==1:
#     print('1')
# elif visited[N-1][M-1] == 0 and breakVisited[N-1][M-1] ==0:
#     print('-1')
# elif visited[N-1][M-1] != 0 and breakVisited[N-1][M-1] ==0:
#     print(visited[N-1][M-1] +1)
# elif visited[N-1][M-1] == 0 and breakVisited[N-1][M-1] !=0:
#     print(breakVisited[N-1][M-1] +1)
#
# else:
#     print(min(visited[N-1][M-1],breakVisited[N-1][M-1])+1 )

# 재채점 후 시간초과. 지금 와서 알아보기도 힘들다

import sys
import collections
sys.setrecursionlimit(10000000)
N,M = map(int,sys.stdin.readline().split())
roadMap = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]



for i in range(N):
    roadMap.append(list(map(int,input())))

def bfs():
    roadStack =collections.deque([])
    roadStack.append((0,0,1))
    visited = [[[0] * 2 for i in range(M)] for i in range(N)]
    visited[0][0][1] =1
    while(roadStack):
        (i,j,wallbreak) = roadStack.popleft()
        if i == N - 1 and j == M - 1:
            return visited[i][j][wallbreak]

        for k in range(4):
            x_d , y_d = i+dx[k], j+dy[k]
            if 0 <= x_d < N and 0 <= y_d < M:
                if roadMap[x_d][y_d] == 0 and visited[x_d][y_d][wallbreak] == 0:
                    roadStack.append((x_d, y_d, wallbreak))
                    visited[x_d][y_d][wallbreak] = visited[i][j][wallbreak] + 1
                if roadMap[x_d][y_d] == 1 and wallbreak == 1:
                    roadStack.append((x_d, y_d, 0))
                    visited[x_d][y_d][0] = visited[i][j][1] + 1

    return -1
print(bfs())