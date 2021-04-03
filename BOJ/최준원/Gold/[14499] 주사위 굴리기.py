from pprint import pprint
R, C, x, y, K = map(int, input().split())
data = [list(map(int, input().split())) for x in range(R)]
moves = list(map(int, input().split()))

# 위, 왼, 탑, 오, 아, 봇
dice = [0] * 6

def spin(direction):
    global dice, x, y

    if direction == 1:
        nc = y + 1
        if nc < C:
            y = nc
            dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
            if data[x][y]:
                dice[5] = data[x][y]
                data[x][y] = 0
            else:
                data[x][y] = dice[5]
            print(dice[2])

    elif direction == 2:
        nc = y - 1
        if nc >= 0:
            y = nc
            dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
            if data[x][y]:
                dice[5] = data[x][y]
                data[x][y] = 0
            else:
                data[x][y] = dice[5]
            print(dice[2])

    elif direction == 3:
        nr = x - 1
        if nr >= 0:
            x = nr
            dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
            if data[x][y]:
                dice[5] = data[x][y]
                data[x][y] = 0
            else:
                data[x][y] = dice[5]
            print(dice[2])
    else:
        nr = x + 1
        if nr < R:
            x = nr
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
            if data[x][y]:
                dice[5] = data[x][y]
                data[x][y] = 0
            else:
                data[x][y] = dice[5]
            print(dice[2])


for move in moves:
    spin(move)