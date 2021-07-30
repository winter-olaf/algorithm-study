import sys
from collections import deque


n, m = map(int, input().split())

# board = [[0 for i in range(m)] for j in range(n)]

board = []

y,x,d = map(int,sys.stdin.readline().split())

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    board.append(temp)

CLEAND = 2
N,E,S,W = 0,1,2,3
cnt =0

direction = [(-1,0),(0,1),(1,0),(0,-1)]


q = deque([])
q.append((y,x))

while(q):
    y,x = q.pop()
    stuck = True

    if board[y][x]==0:
        board[y][x] = CLEAND
        cnt+=1

    for i in range(4):
        d -=1
        if d == -1:
            d = 3
        dy,dx = direction[d]

        ny = y + dy
        nx = x + dx

        if 0<=ny<n and 0<= nx<m:
            if board[ny][nx] == 0:
                q.append((ny,nx))
                stuck = False
                break
    if stuck:
        bd= d-2
        dy, dx = direction[bd]
        ny = y + dy
        nx = x + dx
        if 0<=ny<n and 0<= nx<m:
            if board[ny][nx] == 0 or board[ny][nx] == CLEAND:
                q.append((ny,nx))



print(cnt)