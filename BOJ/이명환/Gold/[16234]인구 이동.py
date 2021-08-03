# import sys
# from collections import deque
# import copy
#
# sys.setrecursionlimit(10**6)
#
# n,l,r = map(int,sys.stdin.readline().split())
#
# land = []
#
# dy = [0,0,-1,1]
# dx = [1,-1,0,0]
#
# for i in range(n):
#     land.append(list(map(int,sys.stdin.readline().split())))
#
#
#
# # for i in range(n*n):
# #     for y in range(n):
# #         for x in range(n):
# #             if is_adjcent[i][y][x]:
# #
#
#
#
# def check_adjcent():
#     adjcented = False
#     fn = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(4):
#                 ny = i + dy[k]
#                 nx = j + dx[k]
#                 if 0 <= ny < n and 0 <= nx < n:
#                     if l <= abs(land[i][j] - land[ny][nx]) <= r:
#                         is_adjcent[fn][ny][nx] = True
#                         adjcented= True
#             fn+=1
#     if adjcented:
#         return True
#     else:
#         return False
#
# def dfs(i):
#     global cnt
#     global population
#     fn = 0
#     for y in range(n):
#         for x in range(n):
#             if is_adjcent[i][y][x]:
#                 if not is_checked[y][x]:
#                     is_checked[y][x] = True
#                     cnt+=1
#                     population += land[y][x]
#                     is_adjcent[i][y][x] = False
#                     dfs(fn)
#             fn+=1
#
# def move(moved_population):
#     for y in range(n):
#         for x in range(n):
#             if is_checked[y][x]:
#                 land[y][x] = moved_population
#
# day =0
# while(True):
#     is_adjcent = [[[False for i in range(n)] for j in range(n)] for k in range(n * n)]
#     if check_adjcent():
#         for i in range(n*n):
#             is_checked = [[False for o in range(n)] for j in range(n)]
#             cnt = 0
#             population = 0
#             dfs(i)
#             if population and cnt:
#                 move_population = int(population/cnt)
#                 move(move_population)
#         day += 1
#     else:
#         break
#
# print(day)
#dfs로 풀려했는데 시간초 제한에 걸려버림

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    move_q = deque()
    q.append([x, y])
    c[x][y] = 1
    people, cnt = 0, 0
    while q:
        x, y = q.popleft()
        move_q.append([x, y])
        people += a[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not c[nx][ny]:
                if l <= abs(a[x][y] - a[nx][ny]) <= r:
                    c[nx][ny] = cnt
                    q.append([nx, ny])

    while move_q:
        x, y = move_q.popleft()
        a[x][y] = people // cnt

    if cnt == 1:
        return 0
    return 1

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    q = deque()
    c = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not c[i][j]:
                cnt += bfs(i, j)
    if not cnt:
        break
    ans += 1

print(ans)