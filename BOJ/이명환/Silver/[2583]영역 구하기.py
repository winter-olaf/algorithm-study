# import sys
# from  collections import deque
# m,n,k = map(int,sys.stdin.readline().split())
# graphPaper =[[0]*n for i in range(m)]
# visited = [[False]*n for _ in range(m)]
# ydir = [-1,1,0,0]
# xdir = [0,0,-1,1]
# for i in range(k):
#     x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
#     y1 = m-y1-1
#     x2 = x2-1
#     y2 = m-y2
#     gap = (abs(x1-x2) , abs(y1-y2))
#     if gap[0] and gap[1]:
#         for row in range(gap[1]+1):
#             for column in range(gap[0]+1):
#                 graphPaper[y2+row][x1+column] = 1
#     elif gap[0]:
#         for column in range(gap[0] + 1):
#             graphPaper[y2][x1 + column] = 1
#     elif gap[1]:
#         for row in range(gap[1]+1):
#             graphPaper[y2+row][x1] = 1
# q = deque([])
# flag = False
#
# cnt = 0
# extent = []
# for r in range(m):
#     for c in range(n):
#         if graphPaper[r][c] ==0 and visited[r][c] == False:
#             q.append((r,c))
#             cnt+=1
#             visited[r][c] = True
#             flag = True
#             break
#     if flag:
#         break
#
# while(q):
#     flag = False
#     row,column = q.popleft()
#
#     for i in range(4):
#         y = ydir[i] + row
#         x = xdir[i] + column
#         if 0<=x<=n-1 and 0<=y<=m-1 and visited[y][x] == False:
#             if graphPaper[y][x] == 0:
#                 visited[y][x] = True
#                 q.append((y,x))
#                 cnt+=1
#     if q:
#         pass
#     else:
#         extent.append(cnt)
#         cnt =0
#         for r in range(m):
#             for c in range(n):
#                 if graphPaper[r][c] == 0 and visited[r][c] == False:
#                     visited[r][c] = True
#                     cnt+=1
#                     q.append((r, c))
#                     flag = True
#                     break
#             if flag:
#                 break
# print(len(extent))
# for i in sorted(extent):
#     print(i,end=' ')
#  50%에서 틀렸다. 생각을 잘못했나. 다른방법을 강구해야할듯 이렇게 설계하는건 너무 번잡한 느낌..

# x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
# y1 = m - y1 - 1
# x2 = x2 - 1
# y2 = m - y2
# gap = (abs(x1 - x2), abs(y1 - y2))
# if gap[0] and gap[1]:
#     for row in range(gap[1] + 1):
#         for column in range(gap[0] + 1):
#             graphPaper[y2 + row][x1 + column] = 1
# elif gap[0]:
#     for column in range(gap[0] + 1):
#         graphPaper[y2][x1 + column] = 1
# elif gap[1]:
#     for row in range(gap[1] + 1):
#         graphPaper[y2 + row][x1] = 1
# 이 부분을 바꾸니 맞았다.. 나는 왤케 이상하게 생각한걸까

import sys
from  collections import deque
m,n,k = map(int,sys.stdin.readline().split())
graphPaper =[[0]*n for i in range(m)]
visited = [[False]*n for _ in range(m)]
ydir = [-1,1,0,0]
xdir = [0,0,-1,1]
for i in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graphPaper[i][j] = 1
q = deque([])
flag = False

cnt = 0
extent = []
for r in range(m):
    for c in range(n):
        if graphPaper[r][c] ==0 and visited[r][c] == False:
            q.append((r,c))
            cnt+=1
            visited[r][c] = True
            flag = True
            break
    if flag:
        break

while(q):
    flag = False
    row,column = q.popleft()

    for i in range(4):
        y = ydir[i] + row
        x = xdir[i] + column
        if 0<=x<=n-1 and 0<=y<=m-1 and visited[y][x] == False:
            if graphPaper[y][x] == 0:
                visited[y][x] = True
                q.append((y,x))
                cnt+=1
    if q:
        pass
    else:
        extent.append(cnt)
        cnt =0
        for r in range(m):
            for c in range(n):
                if graphPaper[r][c] == 0 and visited[r][c] == False:
                    visited[r][c] = True
                    cnt+=1
                    q.append((r, c))
                    flag = True
                    break
            if flag:
                break
print(len(extent))
for i in sorted(extent):
    print(i,end=' ')
#다른 사람의 코드
# #블록이 몇개인지 알아내기 위한 BFS 너비 우선 탐색 함수를 정의
# def bfs(i, j):
#     global visited, paper
#
#     if paper[i][j] == 1: #직사각형 내부일 경우(1일 경우) 함수를 넘김
#         visited.append([i, j])
#         return
#
#     block = [] #함수 안에서만 쓰일 블록
#     queue = [[i, j]] #함수 안에서만 쓰일 큐
#
#     while queue:
#         [i, j] = queue.pop(0)
#         block.append([i, j]) #블록에 쌓아줌
#         visited.append([i, j]) #방문 리스트에 쌓아줌
#
#         if paper[i][j] == 0: #각각 상하좌우를 확인하는 조건문
#             if i < M-1 and paper[i+1][j] == 0 and [i+1, j] not in block and [i+1, j] not in queue:
#                 queue.append([i+1, j])
#             if j < N-1 and paper[i][j+1] == 0 and [i, j+1] not in block and [i, j+1] not in queue:
#                 queue.append([i, j+1])
#             if i > 0 and paper[i-1][j] == 0 and [i-1, j] not in block and [i-1, j] not in queue:
#                 queue.append([i-1, j])
#             if j > 0 and paper[i][j-1] == 0 and [i, j-1] not in block and [i, j-1] not in queue:
#                 queue.append([i, j-1])
#
#     return len(block) #블록의 크기만 출력하면 된다
#
#
# #입력
# M, N, K = map(int, input().split())
# paper = [[0 for _ in range(N)] for _ in range(M)]
#
# #입력 - 직사각형 좌표 내부를 1로 바꾸어줌
# for _ in range(K):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             paper[i][j] = 1
#
#
# #함수 실행
# visited = []
# block_list = []
#
# #0,0 부터 M,N까지 각각의 블록에 관하여 함수 실행문
# for i in range(M):
#     for j in range(N):
#         if [i, j] not in visited:
#             block = bfs(i, j)
#             if block:
#                 block_list.append(block)
# 
#
# #출력문
# print(len(block_list))
# for i in sorted(block_list):
#     print(i, end= ' ')

#내 코드와 비교하여 간결함이 늘었다. 0,0 부터 M,N까지 각각의 블록에 관하여 함수 실행문을 구성할 떄 차이가 있었는듯...
#간결한 코드를 짜도록 노력하자. 새로 고치려고 하니까 너무 막막해서 주저앉을뻔했다.