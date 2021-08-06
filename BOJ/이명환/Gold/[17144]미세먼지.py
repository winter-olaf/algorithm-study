import sys
from collections import deque
import copy


r,c,t = map(int,sys.stdin.readline().split())
room = []
air_cleaner = []

dusts = deque([])
preserve_dusts = []

dy = [0,0,1,-1]
dx = [1,-1,0,0]

for i in range(r):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(c):
        if temp[j] == -1:
            air_cleaner.append((i,j))
        elif temp[j] != 0:
            dusts.append((i,j))
    room.append(temp)

while(t):
    newRoom = [[0 for i in range(c)] for _ in range(r)]

    while(dusts):
        y,x = dusts.popleft()
        diffusion_cnt = 0
        k = int(room[y][x] / 5)
        for m in range(4):
            ny = y + dy[m]
            nx = x + dx[m]
            if 0<=ny< r and 0<= nx < c and room[ny][nx]!=-1:
                    diffusion_cnt +=1
                    newRoom[ny][nx] += k
        newRoom[y][x] += int(room[y][x] -k*diffusion_cnt)
    ay,ax = air_cleaner[0]
    pretemp = newRoom[ay][ax+1]


    for i in range(ax+1,c):
        temp = newRoom[ay][i]
        newRoom[ay][i] = pretemp
        pretemp = temp

    newRoom[ay][ax+1] = 0

    for j in range(ay-1,-1,-1):
        temp = newRoom[j][c-1]
        newRoom[j][c-1] = pretemp
        pretemp = temp


    for i in range(c - 2, -1, -1):
        temp = newRoom[0][i]
        newRoom[0][i] = pretemp
        pretemp = temp

    for j in range(1,ay,1):
        temp = newRoom[j][0]
        newRoom[j][0] = pretemp
        pretemp = temp

    newRoom[ay][ax] = 0

    #-------청정기 아래-------

    ay,ax = air_cleaner[1]
    pretemp = newRoom[ay][ax+1]


    for i in range(ax+1,c):
        temp = newRoom[ay][i]
        newRoom[ay][i] = pretemp
        pretemp = temp

    newRoom[ay][ax+1] = 0

    for j in range(ay+1,r):
        temp = newRoom[j][c-1]
        newRoom[j][c-1] = pretemp
        pretemp = temp

    for i in range(c - 2, -1, -1):
        temp = newRoom[r-1][i]
        newRoom[r-1][i] = pretemp
        pretemp = temp

    for j in range(r-2, ay, -1):
        if j == ay:
            break
        temp = newRoom[j][0]
        newRoom[j][0] = pretemp
        pretemp = temp

    newRoom[ay][ax] = 0


    for i in range(r):
        for j in range(c):
            if newRoom[i][j]:
                dusts.append((i,j))

    t -= 1
    room = newRoom

ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j] !=0 and room[i][j] != -1:
            ans+= room[i][j]
print(ans)