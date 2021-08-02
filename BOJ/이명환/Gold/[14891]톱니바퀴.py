import sys
from collections import deque

gear1 = deque(list(map(int,sys.stdin.readline().rstrip())))
gear2 = deque(list(map(int,sys.stdin.readline().rstrip())))
gear3 = deque(list(map(int,sys.stdin.readline().rstrip())))
gear4 = deque(list(map(int,sys.stdin.readline().rstrip())))

gears = [gear1,gear2,gear3,gear4]

k = int(sys.stdin.readline())

order = deque([])

for i in range(k):
    temp = list(map(int,sys.stdin.readline().split()))
    order.append(temp)

N = 0
S = 1

CLOCKWISE = 1
COUNTER_CLOCKWISE = -1


while(order):
    gearNum, d = order.popleft()
    gearNum -=1

    gear = gears[gearNum]

    originD = d
    originRightPole =gear[2]
    originLeftPole = gear[6]

    rightPole =gear[2]
    leftPole = gear[6]

    if d == CLOCKWISE:
        temp = gear.pop()
        gear.appendleft(temp)
    else:
        temp = gear.popleft()
        gear.append(temp)

    for i in range(gearNum+1,4):
        gear = gears[i]

        if rightPole == gear[6]:
            break
        rightPole = gear[2]

        #반대방향으로 돈다
        if d == CLOCKWISE:
            temp = gear.popleft()
            gear.append(temp)
            d = COUNTER_CLOCKWISE
        else:
            temp = gear.pop()
            gear.appendleft(temp)
            d = CLOCKWISE

    d = originD
    leftPole = originLeftPole

    for i in range(gearNum - 1, -1,-1):
        gear = gears[i]

        if leftPole == gear[2]:
            break

        leftPole = gear[6]

        # 반대방향으로 돈다
        if d == CLOCKWISE:
            temp = gear.popleft()
            gear.append(temp)
            d = COUNTER_CLOCKWISE
        else:
            temp = gear.pop()
            gear.appendleft(temp)
            d = CLOCKWISE

cnt=0

for i in range(4):
    if gears[i][0]== S:
        cnt+= 2**(i)

print(cnt)

#너무 변수를 많이 만들어서 헷갈리기도 하고.. 함수화 시켜야할듯
