from collections import deque
gears = [deque(list(input())) for x in range(4)]
# gear : 12, 1, 3, 5 / 6, 7, 9, 11
k = int(input())
spins = [list(map(int, input().split())) for x in range(k)]
# 1 시계, -1 반시계

for no, di in spins:
    no -= 1 # index
    is_spin = [0] * 4 # 이번에 회전하는가
    spin_di = [0] * 4 # 이번의 회전 방향
    is_spin[no] = 1
    spin_di[no] = di

    cur_no = no
    cur_di = di

    # 시작 기준 왼쪽
    for i in range(no-1, -1, -1):
        if gears[cur_no][6] != gears[i][2]:
            is_spin[i] = 1
            cur_di *= -1
            spin_di[i] = cur_di
            # spin_di[i] = cur_di * -1 # 아 ;; 실수
            cur_no = i
        else:
            break

    cur_no = no
    cur_di = di

    # 시작 기준 오른쪽
    for i in range(no+1, 4):
        if gears[cur_no][2] != gears[i][6]:
            is_spin[i] = 1
            cur_di *= -1
            spin_di[i] = cur_di
            cur_no = i
        else:
            break

    for i in range(4):
        if is_spin[i]:
            if spin_di[i] == 1: # 시계방향 회전 -1이나 1이나 이쪽으로 빠졌기 때문에 틀리고있었다
                gears[i].appendleft(gears[i].pop())
            else: # 반시계방향 회전
                gears[i].append(gears[i].popleft())

res = 0

for i in range(4):
    if gears[i][0] == '1':
        res += 2**i

print(res)