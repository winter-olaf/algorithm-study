# 4008ms
'''
stack = []
for _ in range(int(input())):
    e = int(input())
    if e == 0:
        stack.pop()
    else:
        stack.append(e)
print(sum(stack))
'''
# 108ms
from sys import stdin
stack = []
for _ in range(int(input())):
    e = int(stdin.readline())
    if e == 0:
        stack.pop()
    else:
        stack.append(e)
print(sum(stack))