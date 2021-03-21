from pprint import pprint
from collections import deque

R, C, K = map(int, input().split())
rectangles = []

data = [[0]*C for x in range(R)]

def bfs(r, c):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(r,c)])
    global result
    area = 1

    while queue:
        cr, cc = queue.popleft()
        data[cr][cc] = 1

        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and not data[nr][nc]:
                area += 1
                queue.append((nr, nc))
                visited[nr][nc] = 1

    result.append(area)

for i in range(K):
    sc, sr, ec, er = map(int, input().split())
    for y in range(sr, er):
        for x in range(sc, ec):
            data[y][x] = 1

visited = [[0]*C for x in range(R)]
result = []

for r in range(R):
    for c in range(C):
        if data[r][c] == 0:
            bfs(r,c)

print(len(result))
print(*sorted(result))