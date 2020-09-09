import sys
from collections import deque
M,N,H = map(int,sys.stdin.readline().split())
box = [[] for num in range(H)]
for num in range(H):
    for i in range(N):
        box[num].append(list(map(int,input().split())))
day = [ [[0]*M for i in range(N)] for num in range(H)]
q = deque([])
p = deque([])
cnt = 1
for k in range(H):
    for j in range(N):
        for i in range(M):
            if box[k][j][i] ==1:
                day[k][j][i] =1
                p.append((j,i,k))
            elif box[k][j][i] == -1:
                day[k][j][i] = -1
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while(p or q):
    while(p):
        r,c,k = p.popleft()
        if k-1>=0:
            if box[k-1][r][c] != -1 and day[k-1][r][c] == 0:
                day[k-1][r][c] = cnt
                q.append((r,c,k-1))
        if k+1 <H:
            if box[k+1][r][c] != -1 and day[k+1][r][c] == 0:
                day[k+1][r][c] = cnt
                q.append((r,c,k+1))
        for i in range(4):
            y = dy[i] + r
            x = dx[i] + c
            if 0<=y<=N-1 and 0<=x<=M-1:
                if box[k][y][x] != -1 and day[k][y][x] == 0:
                    day[k][y][x] = cnt
                    q.append((y,x,k))
    if q:
        cnt += 1
    else :
        break
    while (q):
        r,c,k = q.popleft()
        if k-1>=0:
            if box[k-1][r][c] != -1 and day[k-1][r][c] == 0:
                day[k-1][r][c] = cnt
                p.append((r,c,k-1))
        if k+1 <H:
            if box[k+1][r][c] != -1 and day[k+1][r][c] == 0:
                day[k+1][r][c] = cnt
                p.append((r,c,k+1))
        for i in range(4):
            y = dy[i] + r
            x = dx[i] + c
            if 0<=y<=N-1 and 0<=x<=M-1:
                if box[k][y][x] != -1 and day[k][y][x] == 0:
                    day[k][y][x] = cnt
                    p.append((y,x,k))
    if p:
        cnt += 1
    else:
        break
flag = True
for k in range(H):
    for j in range(N):
        for i in range(M):
            if day[k][j][i] == 0:
                print(-1)
                flag = False
                break
        if flag == False:
            break
if flag:
    print(cnt-1)
#시간이 많이 걸리긴 하는데 풀음