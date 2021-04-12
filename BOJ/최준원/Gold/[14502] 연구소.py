from collections import deque
R, C = map(int, input().split())
data = [list(map(int, input().split())) for x in range(R)]

wall_able = []
virus = []
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for i in range(R):
    for j in range(C):
        if not data[i][j]:
            wall_able.append((i,j))
        elif data[i][j] == 2:
            virus.append((i,j))

# 벽을 백트래킹으로 세우고, 3개를 세웠을 경우에는 빠져서 bfs로 안전영역 체크
selected = [0] * 3

def walling(idx, cnt, selected):
    if cnt == 3:
        bfs(selected)
        return

    if idx > len(wall_able)-1:
        return

    selected[cnt] = idx
    walling(idx+1, cnt+1, selected)
    walling(idx+1, cnt, selected)

def bfs(wall_idxs):
    global result
    res = 0
    # 메모리 사용을 줄이기 위해 임시 벽 배열 생성
    tmp_wall = []
    visited = [[0] * C for x in range(R)]

    for idx in wall_idxs:
        r, c = wall_able[idx]
        tmp_wall.append((r,c))
        visited[r][c] = 4

    for vr,vc in virus:
        visited[vr][vc] = 2

    queue = deque(virus)
    while queue:
        cr, cc = queue.popleft()
        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in tmp_wall and not visited[nr][nc] and not data[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = 2
                res += 1

    # 0이었던 자리 - 바이러스가 퍼진 범위 - 가벽
    if len(wall_able) - res - 3 > result:
        result = len(wall_able) - res - 3

result = 0
walling(0,0,selected)

print(result)

