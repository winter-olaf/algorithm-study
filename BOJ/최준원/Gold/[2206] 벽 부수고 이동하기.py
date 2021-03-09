# dfs는 최단 거리임을 보장하지 않기 때문에 안된다.
# def dfs():
#     cnt = 1
#     wall = 1
#     delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     stack = [(0,0)]
#     # N행 M열
#     visited = [[0] * M for x in range(N)]
#
#     while stack:
#         cr, cc = stack[-1]
#
#         if (cr, cc) == e:
#             return cnt
#
#         for dr, dc in delta:
#             nr = cr + dr
#             nc = cc + dc
#             if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
#                 if wall and arr[nr][nc]:
#                     stack.append((nr,nc))
#                     visited[nr][nc] = 1
#                     arr[nr][nc] = 1
#                     cnt += 1
#                     wall -= 1
#                     break
#
#                 elif not arr[nr][nc]:
#                     stack.append((nr, nc))
#                     visited[nr][nc] = 1
#                     arr[nr][nc] = 1
#                     cnt += 1
#                     break
#         else:
#             stack.pop()
#             cnt -= 1
#
#     return -1
#
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for x in range(N)]
# e = (N-1, M-1) # index
# cnt = dfs()

from collections import deque

def bfs():
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0,0,1,1)])
    # 벽을 부술 경우, 부수지 않을 경우 각각의 체크를 위해 3차원 배열을 생성해야 한다!!
    visited = [[[0] * M for x in range(N)] for x in range(2)]
    # 0이 벽을 부순 경우, 1이 벽을 부수지 않았을 경우의 방문 체크 배열이다.
    visited[1][0][0] = 1

    while queue:
        cr, cc, cd, cw = queue.popleft()

        if (cr, cc) == e:
            return cd

        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            # 인덱스를 벗어나지 않는지 체크하고, cw의 상황에 따라 방문 체크 배열을 다르게 본다!
            if 0 <= nr < N and 0 <= nc < M and not visited[cw][nr][nc]:
                # 벽을 부수면서 갔을 경우
                if cw and arr[nr][nc]:
                    queue.append((nr, nc, cd+1, cw-1))
                    # 이곳이 핵심이다. 여기를 그냥 visited[nr][nc]로 해버리면
                    # 벽을 부순다, 부수지 않는다 두 가지 경우를 체크하지 못한다!
                    visited[0][nr][nc] = 1
                # 벽을 부수지 않고 이동할 경우
                elif not arr[nr][nc]:
                    queue.append((nr, nc, cd+1, cw))
                    visited[cw][nr][nc] = 1
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input())) for x in range(N)]
e = (N-1, M-1) # index
cnt = bfs()
print(cnt)

'''
반례
5 5
00000
11101
00000
01111
00010
이게 왜 안되는지 알았다. 1,4,0에서 온 2,4,0이 2,3,1에서 간 2,4,1을 묻어버리는거다.
'''