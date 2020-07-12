# 시간 초과
# from sys import stdin
# n,k = map(int,stdin.readline().split())
# arr = [x for x in range(1,n+1)]
# stack = [x for x in range(1,n+1)]
# deleted = []
# for i in range(1,n+1):
#     idx = k*i-1
#     if idx>len(stack)-1:
#         for i in arr:
#             if i in deleted:
#                 arr.remove(i)
#         while True:
#             if len(stack)>idx:
#                 break
#             stack.extend(arr)
#     if stack[idx] not in deleted:
#         deleted.append(stack[idx])
# print('<',', '.join([str(x) for x in deleted]),'>',sep='')
# 1 2 3 4 5 6 7 1 2 4 5 7 1 4 5 1 4 1 4 4 4 4

# for에 while이 지나치게 많이 반복됨
from sys import stdin
n, k = map(int, stdin.readline().split())
arr = [x for x in range(1, n+1)]
idx = k-1
deleted = []
while arr:
    while idx > len(arr)-1:
        idx -= len(arr)
    deleted.append(arr.pop(idx))
    idx+=(k-1)
print('<', ', '.join([str(x) for x in deleted]), '>', sep='')