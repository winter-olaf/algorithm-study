# import sys
# from collections import deque
# m,n = map(int,sys.stdin.readline().split())
# cheez = [list(map(int,input().split())) for _ in range(m)]
#
# #치즈가 다 사라졌는지 확인
# xdir = [0,1,-1,0]
# ydir = [-1,0,0,1]
#
# day = 0
# remain = 0
# while True:
#     before_remain = remain
#     remain =0
#     visited = [[False] * n for i in range(m)]
#     q = deque((0,0))
#     while q:
#         row,column = q.popleft()
#         if cheez[row][column] != 0:
#             remain +=1
#         elif cheez[row][column] == 0 and visited[row][column] != True:
#             for i in range(4):
#                 x = xdir[i] + column
#                 y = ydir[i] + row
#                 if 0<=x<=n-1 and 0<=y<=m-1:
#                     if cheez[y][x] !=0 and cheez[y][x] !=0:
#                         cheez[y][x] = 0
#                         visited[y][x] = True
#     day +=1
#     if remain == 0:
#         print(day)
#         print(before_remain)
#         break
#
#     # 함수로 구현하는게 나을듯? 큐로 하니까 날짜 구분이 어려운 것 같다.


import sys
sys.setrecursionlimit(111111)
m,n = map(int,sys.stdin.readline().split())
cheez = [list(map(int,input().split())) for _ in range(m)]

#치즈가 다 사라졌는지 확인
xdir = [0,1,-1,0]
ydir = [-1,0,0,1]

day = 0
no_cheez = 0
def dfs(row, column):
    for i in range(4):
        x = xdir[i] + column
        y = ydir[i] + row
        if 0 <= x <= n - 1 and 0 <= y <= m - 1:
            if cheez[y][x] != 0 and visited[y][x] == False:
                cheez[y][x] = 0
                visited[y][x] = True
            elif cheez[y][x] ==0 and visited[y][x] == False:
                visited[y][x] = True
                dfs(y, x)

while True:
    previous_cheez = 0
    for i in range(m):
        for j in range(n):
            if cheez[i][j] !=0:
                previous_cheez +=1
    visited = [[False] * n for i in range(m)]
    dfs(0,0)
    no_cheez = 0
    for i in range(m):
        for j in range(n):
            if cheez[i][j] ==0:
                no_cheez +=1
    day +=1
    if no_cheez == n*m:
        print(day)
        print(previous_cheez)
        break

#번잡하다 개선의 여지가 있을듯? 특히 previous_cheez와 no_cheez를 구하는 것에..
#https://it-garden.tistory.com/274 이게 제일 깔끔한듯