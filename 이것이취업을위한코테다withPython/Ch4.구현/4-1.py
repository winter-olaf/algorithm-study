# 상하좌우
n = int(input())
plans = input().split()
x,y = 1,1

# L, R, U, D 이동 값
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L','R','U','D']

for plan in plans:
    for i in range(4):
        if move[i] == plan:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x = nx
    y = ny
print(x,y)