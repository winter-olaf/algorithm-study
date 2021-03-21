from collections import deque
def bfs(n, m):
    visited = [[0] * M for x in range(N)]
    queue = deque([(0, 0, 1)])
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        cr, cc, cd = queue.popleft()

        if (cr, cc) == (n, m):
            return cd

        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
                queue.append((nr,nc,cd+1))
                visited[nr][nc] = 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for x in range(N)]
res = bfs(N-1, M-1)
print(res)