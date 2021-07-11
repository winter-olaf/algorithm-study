import sys
from collections import deque

n = int(sys.stdin.readline())
board = list([ 0 for i in range(n)] for j in range(n))
k = int(sys.stdin.readline())
for i in range(k):
    y,x = map(int,sys.stdin.readline().split())
    y-=1
    x-=1
    board[y][x] = 2 #사과는 2 꼬리는 1

l = int(sys.stdin.readline())
order = deque([])
for i in range(l):
    time,instruct= sys.stdin.readline().split()
    order.append((int(time),instruct))

gameTime = 0
direction = [(1,0),(0,1),(-1,0),(0,-1)]
direction_num = 0
snake_x = 0
snake_y = 0
snake_body = deque([])
snake_length = 1

while(True):
    gameTime+=1
    move_x,move_y = direction[direction_num]
    board[snake_y][snake_x] =1
    snake_body.append((snake_y,snake_x))

    if len(snake_body) > snake_length:
        tail_y,tail_x = snake_body.popleft()
        board[tail_y][tail_x] =0

    if 0<=snake_x+move_x<=n-1 and 0<=snake_y+move_y <=n-1:
        snake_x+= move_x
        snake_y+= move_y
        if board[snake_y][snake_x]== 1: #꼬리
            break
        elif board[snake_y][snake_x] ==2: #사과
            snake_length+=1
    else: #벽
        break


    if order:
        time,direct = order.popleft()
        if gameTime==time:
            if direct== 'D':
                direction_num+=1
                if direction_num== 4:
                    direction_num = 0
            elif direct == 'L':
                direction_num-=1
                if direction_num == -1:
                    direction_num = 3
        else:
            order.appendleft((time,direct))

print(gameTime)