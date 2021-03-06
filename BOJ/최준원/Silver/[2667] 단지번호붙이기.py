# DFS
# N = int(input())
# arr = [list(map(int, input())) for x in range(N)]
#
# delta = [(0, 1), (0, -1), (1, 0), (-1,0)]
# def dfs(r,c):
#     global res
#     visited = [[0] * N for x in range(N)]
#     cnt = 1
#     stack = [(r,c)]
#     visited[r][c] = 1
#     #
#     # while stack:
#     #     top = stack[-1]
#     #     cr = top[0]
#     #     cc = top[1]
#     #     for dr,dc in delta:
#     #         nr = cr + dr
#     #         nc = cc + dc
#     #         if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
#     #             stack.append((nr,nc))
#     #             arr[nr][nc] = 0
#     #             visited[nr][nc] = 1
#     #             cnt += 1
#     #             break # 아!!!!!! 이거 하나 안넣어서 경로 찾은 뒤에 즉시 그 경로로 이동하질 않았다 ㅠㅠㅠ
#     #     else:
#     #         stack.pop()
#
#     while stack:
#         top = stack.pop()
#         cr = top[0]
#         cc = top[1]
#         for dr,dc in delta:
#             nr = cr + dr
#             nc = cc + dc
#             if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
#                 stack.append((nr,nc))
#                 arr[nr][nc] = 0
#                 visited[nr][nc] = 1
#                 cnt += 1
#
#     res.append(cnt)
#
# res = []
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:
#             dfs(i,j)
#
# print(len(res))
# for i in sorted(res):
#     print(i)

# BFS

from collections import deque
N = int(input())
arr = [list(map(int, input())) for x in range(N)]

delta = [(0, 1), (0, -1), (1, 0), (-1,0)]

def bfs(r,c):
    global res
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True

    queue = deque([(r, c)])
    cnt = 1

    while queue:
        cr, cc = queue.popleft()

        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == False:
                arr[nr][nc] = 0
                queue.append((nr, nc))
                visited[cr][cc] = True
                cnt += 1

    res.append(cnt)
    return

res = []

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            bfs(i,j)

print(len(res))
for i in sorted(res):
    print(i)