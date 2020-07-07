# 76ms / 29380KB
# from sys import stdin
# Q = []
# def queue(i):
#     cmd = i[0]
#     if cmd == "push":
#         Q.append(int(i[1]))
#     if cmd == "pop":
#         if Q:
#             return Q.pop(0)
#         else:
#             return -1
#     if cmd == "size":
#         return len(Q)
#     if cmd == "front":
#         if Q:
#             return Q[0]
#         else:
#             return -1
#     if cmd == "back":
#         if Q:
#             return Q[-1]
#         else:
#             return -1
#     if cmd == "empty":
#         return 0 if Q else 1
# n = int(input())
# result = []
# for i in range(n):
#     res = queue(list(map(str, stdin.readline().split())))
#     if res != None:
#         result.append(res)
# for i in result:
#     print(i)

# 데큐를 이용한 풀이

# 100ms / 31824KB
from sys import stdin
from collections import deque
Q = deque()
def queue(i):
    cmd = i[0]
    if cmd == "push":
        Q.append(int(i[1]))
    if cmd == "pop":
        if Q:
            return Q.popleft()
        else:
            return -1
    if cmd == "size":
        return len(Q)
    if cmd == "front":
        if Q:
            return Q[0]
        else:
            return -1
    if cmd == "back":
        if Q:
            return Q[-1]
        else:
            return -1
    if cmd == "empty":
        return 0 if Q else 1
n = int(input())
result = []
for i in range(n):
    res = queue(list(map(str, stdin.readline().split())))
    if res != None:
        result.append(res)
for i in result:
    print(i)