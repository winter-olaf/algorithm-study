# import sys
#
# n = int(sys.stdin.readline())
# card_list = list(map(int,sys.stdin.readline().split()))
# dp = [0 for i in range(n+1)]
# dp[1] = card_list[0]
#
# if n == 2:
#     dp[n] = max(card_list[0]+card_list[0],card_list[1])
# elif n!=1:
#     for i in range(2,n+1):
#         if i%2 ==0:
#            dp[i] = max(card_list[i-1],dp[i-1]+card_list[0],dp[int(i/2)]+card_list[int(i/2)-1])
#         else:
#             dp[i] = max(card_list[i-1],dp[i-1]+card_list[0])
# print(dp[n])


import sys

n = int(sys.stdin.readline())
card_list = [0]+list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i - j] + card_list[j])

print(dp[n])