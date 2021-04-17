C, R, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for x in range(R)] for y in range(H)]
visited = [[[0]*C for x in range(R)] for y in range(H)]

from collections import deque

delta = [(0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,0,1), (0,0,-1)]

def bfs(arr):
    global res, visited, tomatoes
    q = deque(arr)

    for a in arr:
        visited[a[0]][a[1]][a[2]] = 1

    while q:
        ch, cr, cc, cd = q.popleft()
        if cd > res:
            res = cd

        for dr,dc,dh in delta:
            nr = cr + dr
            nc = cc + dc
            nh = ch + dh
            if 0 <= nr < R and 0 <= nc < C and 0 <= nh < H and not visited[nh][nr][nc] and tomatoes[nh][nr][nc] == 0:
                q.append((nh, nr, nc, cd+1))
                tomatoes[nh][nr][nc] = 1
                visited[nh][nr][nc] = 1
    return

res = 0

arr = []

for h in range(H):
    for r in range(R):
        for c in range(C):
            # 1을 찾으면 바로 bfs를 시작하는게 아니라 1을 모두 다 찾은 뒤에 한꺼번에 큐에 넣고 탐색을 시작해야 한다.
            if tomatoes[h][r][c] == 1:
                arr.append((h, r, c, 0))

bfs(arr)

for h in range(H):
    for r in range(R):
        for c in range(C):
            if tomatoes[h][r][c] == 0:
                res = -1
                break

print(res)

'''
반례
1이 여러개라면 그걸 모두 다 큐에 넣고 시작해야 한다

5 3 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
'''