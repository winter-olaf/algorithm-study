import sys
from collections import deque
import copy

n,m = map(int,sys.stdin.readline().split())

office = []
cctv = deque([])
wall = []

UP,RIGHT,DOWN,LEFT, = 0,1,2,3

cctv_works = [[],
  [
    [RIGHT],
    [LEFT],
    [UP],
    [DOWN]
],[
    [LEFT,RIGHT],
    [UP,DOWN]
],[
    [UP,RIGHT],
    [RIGHT,DOWN],
    [DOWN,LEFT],
    [LEFT,UP]
],[
    [LEFT,UP,RIGHT],
    [UP,RIGHT,DOWN],
    [RIGHT,DOWN,LEFT],
    [DOWN,LEFT,UP]
],[
    [LEFT,UP,RIGHT,DOWN]
]]

CHECKED = 9
min_cnt = 99999

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if 1<=temp[j]<=5:
            cctv.append((i,j,temp[j]))
        elif temp[j] == 6:
            wall.append((i,j))

    office.append(temp)

def watcharea(cctv,office):
    global min_cnt
    newCctv = copy.deepcopy(cctv)
    if newCctv:
        cy,cx,cn = newCctv.popleft()
        for i in cctv_works[cn]:
            newOfice = copy.deepcopy(office)
            slots = i
            for j in slots:
                if j == UP:
                    for u in range(cy,-1,-1):
                        if newOfice[u][cx] == 6:
                            break
                        newOfice[u][cx] = CHECKED

                elif j == RIGHT:
                    for u in range(cx, m):
                        if newOfice[cy][u] == 6:
                            break
                        newOfice[cy][u] = CHECKED
                elif j == DOWN:
                    for u in range(cy, n):
                        if newOfice[u][cx] == 6:
                            break
                        newOfice[u][cx] = CHECKED
                elif j == LEFT:
                    for u in range(cx, -1, -1):
                        if newOfice[cy][u] == 6:
                            break
                        newOfice[cy][u] = CHECKED
            watcharea(newCctv,newOfice)
    else:
        cnt =0
        for i in range(n):
            cnt += office[i].count(0)
        if cnt < min_cnt:
            min_cnt = cnt


watcharea(cctv,office)


print(min_cnt)

##cctv 조건에 실수가 있어서 도전에 2번 실패함;