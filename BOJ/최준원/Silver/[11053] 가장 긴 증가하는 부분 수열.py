n = int(input())
arr = list(map(int, input().split()))

# O(N^2)
dp = [1] * (n)
res = 0

for i in range(n):
    here = 0
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

    res = max(dp[i], res)

print(res)