from collections import deque
N = int(input())

data = [list(input()) for x in range(N)]
rg_data = data

def bfs(r,c,rg):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0]*N for x in range(N)]

    queue = deque([(r, c, data[r][c])])

    if rg:
        while queue:
            cr, cc, color = queue.popleft()
            data[cr][cc] = 'X'
            for dr, dc in delta:
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[0][nr][nc] and rg_data[nr][nc] == color:
                    queue.append((nr, nc, color))
                    visited[nr][nc] = 1
    else:
        while queue:
            cr, cc, color = queue.popleft()
            data[cr][cc] = 'X'
            for dr, dc in delta:
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[0][nr][nc] and data[nr][nc] == color:
                    queue.append((nr, nc, color))
                    visited[nr][nc] = 1



res = 0
res_rg = 0

for r in range(N):
    for c in range(N):
        if data[r][c] != 'X':
            bfs(r,c,0)
            res += 1

for r in range(N):
    for c in range(N):
        if rg_data[r][c] != 'X':
            bfs(r,c,1)
            res_rg += 1
