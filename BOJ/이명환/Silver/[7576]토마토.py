import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())
box = []
for i in range(N):
    box.append(list(map(int,input().split())))
day = [[0]*M for i in range(N)]
q = deque([])
p = deque([])
cnt = 1
for j in range(N):
    for i in range(M):
        if box[j][i] ==1:
            day[j][i] =1
            p.append((j,i))
        elif box[j][i] == -1:
            day[j][i] = -1
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while(p or q):
    while(p):
        r,c = p.popleft()
        for i in range(4):
            y = dy[i] + r
            x = dx[i] + c
            if 0<=y<=N-1 and 0<=x<=M-1:
                if box[y][x] != -1 and day[y][x] == 0:
                    day[y][x] = cnt
                    q.append((y,x))
    if q:
        cnt += 1
    else :
        break
    while (q):
        r, c = q.popleft()
        for i in range(4):
            y = dy[i] + r
            x = dx[i] + c
            if 0 <= y <= N - 1 and 0 <= x <= M-1:
                if box[y][x] != -1 and day[y][x] == 0:
                    day[y][x] = cnt
                    p.append((y, x))
    if p:
        cnt += 1
    else:
        break
flag = True
for j in range(N):
    for i in range(M):
        if day[j][i] == 0:
            print(-1)
            flag = False
            break
    if flag == False:
        break
if flag:
    print(cnt-1)