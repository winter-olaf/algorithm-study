from collections import deque
N = int(input())
arr = [[0]*N for x in range(N)]
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

snake_moves = ['']*10001
L = int(input())
for _ in range(L):
    sec, di = input().split()
    snake_moves[int(sec)] = di

# snake = 0, 0
# 오른쪽부터 시계방향
delta = [(0,1),(1,0),(0,-1),(-1,0)]
# L => -1, D => +1
direction = 0 # +4 if delta < 0

res = 0

snake = deque([(0,0)])
while 1:
    res += 1
    cr, cc = snake[-1]

    if direction < 0:
        direction += 4

    nr = cr + delta[direction%4][0]
    nc = cc + delta[direction%4][1]

    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in snake:
        if arr[nr][nc]:
            # 사과 먹고 그 위치 0으로 바꿔주기를 안했다.
            arr[nr][nc] = 0
        else:
            snake.popleft()
        snake.append((nr,nc))
    # 이동하다가 벽을 만나거나 자기 몸통을 만나면
    else:
        break

    # 방향전환
    if snake_moves[res] == 'L':
        direction -= 1
    elif snake_moves[res] == 'D':
        direction += 1

print(res)