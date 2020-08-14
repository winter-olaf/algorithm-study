# import sys
# from collections import deque
#
#
# N,M = map(int, sys.stdin.readline().split())
# matrix = [list(map(int, list(input()))) for _ in range(N)]
# global cnt
# cnt = 0
# cnt_list = []
#
# def moveForDirect(i,j,a):
#     global cnt
#     a[i][j] =0
#     if (i,j) == (N-1,M-1):
#         cnt_list.append(cnt)
#         cnt =0
#         return
#     #상
#     if i-1 >=0 and a[i-1][j] != 0:
#         cnt+=1
#         moveForDirect(i-1,j,a)
#     #하
#     if i+1 <=N-1 and a[i+1][j] != 0:
#         cnt +=1
#         moveForDirect(i+1,j,a)
#     #좌
#     if j-1 >=0 and a[i][j-1] != 0:
#         cnt +=1
#         moveForDirect(i,j-1,a)
#     #우
#     if j+1 <=M-1 and a[i][j+1] != 0:
#         cnt +=1
#         moveForDirect(i,j+1,a)
# moveForDirect(0,0,matrix)
# print(cnt_list)
# matrix가 공유되면서 하나의 값만 나옴 .. 그것도 최솟값이 아니다
import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
def BFS(matrix,i,j,N,M):
    visit = []
    queue = deque([[i,j]])
    distance = [[0]*M for _ in range(N)]
    distance[0][0] =1
    while queue:
        [i,j] = queue.popleft()
        visit.append([i,j])

        if i >0 and matrix[i-1][j] ==1 and [i-1,j] not in visit and [i-1,j] not in queue:
            queue.append([i-1,j])
            distance[i-1][j] = distance[i][j] +1
        if i < N-1 and matrix[i + 1][j] == 1 and [i + 1,j] not in visit and [i + 1,j] not in queue:
            queue.append([i +1, j])
            distance[i+1][j] = distance[i][j] + 1
        if j > 0 and matrix[i][j-1] == 1 and [i,j-1] not in visit and [i,j-1] not in queue:
            queue.append([i, j-1])
            distance[i][j-1] = distance[i][j] + 1
        if j < M-1 and matrix[i][j+1] == 1 and [i,j + 1] not in visit and [i,j + 1] not in queue:
            queue.append([i, j + 1])
            distance[i][j + 1] = distance[i][j] + 1
    return distance[N-1][M-1]
print(BFS(matrix,0,0,N,M))








