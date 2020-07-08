# 
from sys import stdin
n,k = map(int,stdin.readline().split())
arr = [x for x in range(1,n+1)]
stack = [x for x in range(1,n+1)]
deleted = []
print('<',end='')
for i in range(1,n+1):
    idx = k*i-1
    # print(stack)
    if idx>len(stack):
        for i in deleted:
            arr.remove(i)
        deleted = []
        print(arr)
        stack.extend(arr)
    deleted.append(stack[idx])
    # print(stack[idx],end=' ')
print('>')

# 1 2 3 4 5 6 7 1 2 4 5 7 1 4 5 1 4 1 4 4 4 4
