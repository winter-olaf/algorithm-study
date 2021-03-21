from collections import deque
import copy
from pprint import pprint
N = int(input())

data = [list(input()) for x in range(N)]
rg_data = copy.deepcopy(data)

def bfs(r,c,rg):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0]*N for x in range(N)]
    visited[r][c] = 1

    if rg: # 적록색맹
        queue = deque([(r, c, rg_data[r][c])])

        while queue:
            cr, cc, color = queue.popleft()
            rg_data[cr][cc] = 'X'
            for dr, dc in delta:
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and rg_data[nr][nc] != 'X':
                    if color in ['G', 'R'] and rg_data[nr][nc] in ['G', 'R']:
                        queue.append((nr, nc, rg_data[nr][nc]))
                        visited[nr][nc] = 1
                    elif color == 'B' and rg_data[nr][nc] == 'B':
                        queue.append((nr, nc, rg_data[nr][nc]))
                        visited[nr][nc] = 1
    else:
        queue = deque([(r, c, data[r][c])])

        while queue:
            cr, cc, color = queue.popleft()
            data[cr][cc] = 'X'
            for dr, dc in delta:
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and data[nr][nc] == color:
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
print(res, res_rg)