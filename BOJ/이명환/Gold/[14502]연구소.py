import sys,copy
from collections import deque

n, m = map(int, input().split())

board = [[0 for i in range(m)] for j in range(n)]

empty_list = []
virus_list = []
max_security = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    stuff = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        board[i][j] = stuff[j]
        if board[i][j] == 0:
            empty_list.append((i,j))
        elif board[i][j] == 2:
            virus_list.append((i,j))

def bfs(nboard):
    global max_security
    q = deque([])
    for virus in virus_list:
        q.append(virus)

    cnt = 0
    visited = [[False]*m for _ in range(n)]

    while(q):
        y,x=q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if ny <0 or ny >=n or nx <0 or nx >=m:
                continue


            if nboard[ny][nx]== 0 and visited[ny][nx]==False:
                q.append((ny,nx))
                nboard[ny][nx] = 2
                visited[ny][nx] = True

    for i in range(n):
        cnt += nboard[i].count(0)

    if max_security < cnt:
        max_security = cnt


for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            board[y1][x1] = 1
            board[y2][x2] = 1
            board[y3][x3] = 1

            nboard = copy.deepcopy(board)
            bfs(nboard)

            board[y1][x1] = 0
            board[y2][x2] = 0
            board[y3][x3] = 0

print(max_security)
