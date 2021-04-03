T = int(input())
data = [int(input()) for x in range(T)]

# 4일때 7이라는게 힌트
# n-1, n-2, n-3 까지의 조합의 합
# dp[n] = dp[n-1], dp[n-2], dp[n-3]
# dp[3]
# 1+1+1
# 1+2
# 2+1
# 3
# dp[2]
# 1+1
# 2
# dp[1]
# 1

memo = [0] * 11
memo[0], memo[1], memo[2] = 1, 2, 4

def dp(n):
    global memo

    if n <= 3:
        return memo[n-1]
    else:
        if memo[n-1]:
            return memo[n-1]
        else:
            res = dp(n-1) + dp(n-2) + dp(n-3)
            memo[n-1] = res
            return res

for i in data:
    dp(i)
    print(memo[i-1])
