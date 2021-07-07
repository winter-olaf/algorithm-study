# import sys
# from collections import deque
#
# n,k = map(int,sys.stdin.readline().split())
# container = list(map(int,sys.stdin.readline().split()))
# step = 0
# robots = deque([])
# await_robots = deque([])
# count = 0
#
# #
#
# while(count < k):
#     temp2 = container[0]
#     for i in range(n*2):
#         temp1 = temp2
#         if i == (n*2-1):
#             container[0] = temp1
#         else:
#             temp2 = container[i + 1]
#             container[i+1] = temp1
#
#     while(robots) :
#        robot = robots.popleft()
#        #로봇이 내리는 위치에 왔을경우
#        if  robot == n-1 :
#            pass
#        #로봇이 한칸 더가면 내려가는 위치일경우
#        elif  robot+1 == n-1 and container[robot+1]:
#            container[robot+1] -=1
#        #로봇이 다음 컨테이너로 넘어갈 수 있는경우
#        elif container[robot+1] and robot+1 not in await_robots:
#            container[robot + 1] -=1
#            await_robots.append(robot+1)
#        #이동을 못할경우
#        else:
#            await_robots.append(robot)
#
#
#     while(await_robots):
#         robots.append(await_robots.popleft()+1)
#     if container[0] and 1 not in await_robots:
#         container[0] -= 1
#         robots.append(1)
#     count = 0
#     for i in range(n*2):
#         if container[i] == 0:
#             count +=1
#     step +=1
#
#
#
#
# print(step)

#시간초과 pypy하면 맞긴함..

import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))

ans = 1

robot = deque(list([0] * n))

while True:  # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    # 1단계 벨트가 한 칸 회전한다.
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    # print('1단계')
    # print(robot)
    # print(arr)
    # 2단계 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(-2, -n - 1, -1):

        if robot[i] == 1 and robot[i + 1] == 0 and arr[i + 1 - n] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            arr[i + 1 - n] -= 1
    robot[-1] = 0
    # print('2단계')
    # print(robot)
    # print(arr)
    # 3단계 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == 0 and arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1
    # print('3단계')
    # print(robot)
    # print(arr)
    # 4단계
    if arr.count(0) >= k:
        break
    ans += 1

print(ans)

#훨씬 코드가 간결하다. deque을 2개만들어 rotate를 돌리는게 간결한 코드의 핵심이였다.
#나는 큐로 구현했는데ㅜ 이 떄문에 코드가 복잡해지고 시간이 많이 걸렸다
#그리고 문제를 잘못 이해해서 많이 해멨다.. 이틀에 걸쳐서 풀음ㅋㅋ