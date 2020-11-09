# import sys
#
# n = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().split()))
# dp = [ 0 for i in range(n)]
# count = 0
# max = 0
# for i in range(1,n):
#     for j in range(i,n):
#         if arr[j-1] < arr[j]:
#             count +=1
#     if(max < count):
#         max = count
#         count=0
# print(max)

import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = [0]*n

for i in range(n):
    if i ==0:
        dp[i] =1
    else:
        max_dp = 0
        for j in range(i):
            if max_dp <dp[j] and arr[j] < arr[i]:
                max_dp = dp[j]
        dp[i] = max_dp +1


print(max(dp))