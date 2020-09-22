# 게임 개발
n, m = map(int,input().split())
x, y, direction = map(int, input().split())

check  = [[0]*m for _ in range(n)]
check[x][y] = 1 # 현재 좌표 방문 처리
game_map = [list(map(int,input().split())) for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Turn to left
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# Start simulation
count = 1
turn_time = 0
while True:
    # Turn to left
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if game_map[nx][ny] == 0 and check[nx][ny] == 0:
        check[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        # continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 뒤로 갈 수 있다면 이동
        nx = x - dx[direction]
        ny = y - dy[direction]
        if check[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        # 뒤가 바다로 막혀있는 경우 시뮬레이션 종료
        else:
            break
        
print(count)
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''