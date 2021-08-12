import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

move_info = deque([])


#비구름 생성

cloud_coordiante = deque([])
cloud_coordiante.append((n,1))
cloud_coordiante.append((n,2))
cloud_coordiante.append((n-1,1))
cloud_coordiante.append((n-1,2))


board = [ [0 for i in range(n+1)] for j in range(n+1)]

dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

diagonal_y = [-1,-1,1,1]
diagonal_x = [-1,1,-1,1]

water_copy = []



for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    for k in range(n):
        board[i+1][k+1] = temp[k]



for i in range(m):
    d,s = map(int,sys.stdin.readline().split())
    move_info.append((d,s))



while(move_info):
    cloud_location = [[False for i in range(n + 1)] for j in range(n + 1)]
    d,s = move_info.popleft()
    while(cloud_coordiante):
        y,x = cloud_coordiante.pop()
        ny = y+ s*dy[d]
        nx = x + s*dx[d]

        if ny < 1:
            ny = n - abs(ny) % n
        elif ny > n:
            ny = ny % n
            if ny == 0:
                ny = n
        if nx < 1:
            nx = n - abs(nx) % n
        elif nx > n:
            nx = nx % n
            if nx == 0:
                nx = n

        board[ny][nx] +=1
        cloud_location[ny][nx] = True
        water_copy.append((ny,nx))

    while(water_copy):
        cnt = 0
        ny,nx = water_copy.pop()
        for i in range(4):
            di_y = ny + diagonal_y[i]
            di_x = nx + diagonal_x[i]
            if 1<=di_y<=n and 1<=di_x<=n:
                if board[di_y][di_x]:
                    cnt+=1
        board[ny][nx] +=cnt



    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j]>=2 and not cloud_location[i][j]:
                cloud_coordiante.append((i,j))
                board[i][j] -=2



ans = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if board[i][j]:
            ans += board[i][j]

print(ans)






