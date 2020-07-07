# 76ms / 29380KB
from sys import stdin 
stack = []
def stacking(i):
    cmd = i[0]
    if cmd == "push":
        stack.append(int(i[1]))
    if cmd == "pop":
        if stack:
            return stack.pop()
        else:
            return -1
    if cmd == "size":
        return len(stack)
    if cmd == "top":
        if stack:
            return stack[-1]
        else:
            return -1
    if cmd == "empty":
        return 0 if stack else 1

n = int(input())
result=[]
for i in range(n):
    res = stacking(list(map(str,stdin.readline().split())))
    if res != None:
        result.append(res)
for i in result:
    print(i)