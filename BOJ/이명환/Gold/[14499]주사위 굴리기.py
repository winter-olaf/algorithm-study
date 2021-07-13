import sys
from collections import deque

n,m,y,x,k = map(int,sys.stdin.readline().split())
board = list([ 0 for i in range(m)] for j in range(n))


for i in range(n):
    board_num = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        board[i][j] = board_num[j]

instructions = deque(list(map(int,sys.stdin.readline().split())))

dice_row = [0,0,0]
dice_col = [0,0,0,0]
direction = [(0,0),(0,1),(0,-1),(-1,0),(1,0)] #y,x

while(instructions):
    ins = instructions.popleft()
    move_y,move_x = direction[ins]
    if 0<=x +move_x <=m-1 and 0<=y + move_y <=n-1:
        x += move_x
        y += move_y

        #주사위 변환
        if ins==1:
            temp = dice_row[2]
            dice_row[2] = dice_row[1]
            dice_row[1] = dice_row[0]
            dice_row[0] = dice_col[3]
            dice_col[3] = temp
            dice_col[1] = dice_row[1]
        elif ins==2:
            temp = dice_row[0]
            dice_row[0] = dice_row[1]
            dice_row[1] = dice_row[2]
            dice_row[2] = dice_col[3]
            dice_col[3] = temp
            dice_col[1] = dice_row[1]
        elif ins==3:
            temp = dice_col[0]
            dice_col[0] = dice_col[1]
            dice_col[1] = dice_col[2]
            dice_col[2] = dice_col[3]
            dice_col[3] = temp
            dice_row[1] = dice_col[1]
        elif ins==4:
            temp = dice_col[3]
            dice_col[3] = dice_col[2]
            dice_col[2] = dice_col[1]
            dice_col[1] = dice_col[0]
            dice_col[0] = temp
            dice_row[1] = dice_col[1]

        if board[y][x]==0:
            board[y][x] = dice_col[3]
        else:
            dice_col[3] = board[y][x]
            board[y][x] = 0

        # print(dice_col)
        # print(dice_row)
        #
        print(dice_col[1])
