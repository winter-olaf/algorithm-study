from collections import deque
LEFT_DOWN = 0 # 2
RIGHT_UP = 1 # 2
DOWN = 2 # 1
RIGHT = 3 # 1
dx = [1, -1, 1, 0]
dy = [-1, 1, 0, 1]

def solution(n, horizontal):
    x, y = 0, 0
    direction = 0
    
    if (horizontal):
        direction = RIGHT
    else:
        direction = DOWN
    x += dx[direction]
    y += dy[direction]    
    r_map = []
    for _ in range(n):
        r_map.append([0 for x in range(n)])
    time = 0
    while 1:
        if x == n - 1 and y == n - 1:
            break
        r_map[x][y] = time
        if direction == RIGHT:
            time += 1
            x += dx[RIGHT]
            y += dy[RIGHT]
            if ((n - 1 >= (x + dx[LEFT_DOWN]) >= 0) and (n - 1 >= (y + dy[LEFT_DOWN]) >= 0)):
                direction = LEFT_DOWN
            else:
                direction = RIGHT_UP
        elif direction == DOWN:
            time += 1
            x += dx[DOWN]
            y += dy[DOWN]
            if ((n - 1 >= (x + dx[RIGHT_UP]) >= 0) and (n - 1 >= (y + dy[RIGHT_UP]) >= 0)):
                direction = RIGHT_UP
            else:
                direction = LEFT_DOWN
        elif direction == RIGHT_UP:
            time += 2
            x += dx[RIGHT_UP]
            y += dy[RIGHT_UP]
            if ((n - 1 >= (x + dx[RIGHT_UP]) >= 0) and (n - 1 >= (y + dy[RIGHT_UP]) >= 0)):
                direction = RIGHT_UP
            elif ((n - 1 >= (x + dx[RIGHT]) >= 0) and (n - 1 >= (y + dy[RIGHT]) >= 0)):
                direction = RIGHT
            else:
                direction = LEFT_DOWN
        elif direction == LEFT_DOWN:
            time += 2
            x += dx[LEFT_DOWN]
            y += dy[LEFT_DOWN]
            if ((n - 1 >= (x + dx[LEFT_DOWN]) >= 0) and (n - 1 >= (y + dy[LEFT_DOWN]) >= 0)):
                direction = LEFT_DOWN
            elif ((n - 1 >= (x + dx[DOWN]) >= 0) and (n - 1 >= (y + dy[DOWN]) >= 0)):
                direction = DOWN
            else:
                direction = RIGHT_UP
    return (r_map)

print(solution(4, True))