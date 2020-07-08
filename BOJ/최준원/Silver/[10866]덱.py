# 96ms / 31824KB
from sys import stdin
from collections import deque
Q = deque()
def queue(i):
    cmd = i[0]
    if cmd == "push_front":
        Q.appendleft(int(i[1]))
    if cmd == "push_back":
        Q.append(int(i[1]))
    if cmd == "pop_front":
        if Q:
            return Q.popleft()
        else:
            return -1
    if cmd == "pop_back":
        if Q:
            return Q.pop()
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