# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# kind = [0 for i in range(n)]
# price_list = []
# kind_lists = []
# answer = 0
# price_sum = 0
# for i in range(n):
#     price_list.append(int(sys.stdin.readline()))
#
#
# def combination_price(price_sum, kind):
#     global answer
#     if (price_sum == k and kind not in kind_lists):
#         answer += 1
#         kind_lists.append(kind)
#         return 0
#     elif (price_sum > k):
#         return 0
#     for order, i in enumerate(price_list):
#         kind[order] += 1
#         combination_price(price_sum+i, kind)
#
#
# combination_price(price_sum, kind)
# print(answer)

import sys

n, k = list(map(int, sys.stdin.readline().split()))
value = []
for i in range(n):
    temp = int(sys.stdin.readline())
    value.append(temp)

dp = [0 for i in range(10001)]
dp[0] = 1
for i in value:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])
