import sys
n = int(sys.stdin.readline())
t,p = [0 for i in range(n+1)],[0 for i in range(n+1)]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    t[i] = a
    p[i] = b

dp = [0 for i in range(n+1)]

for i in range(len(t)-2,-1,-1):
    if t[i]+i <= n:
        dp[i] = max(p[i]+dp[i+t[i]], dp[i+1])
    else:
        dp[i]=dp[i+1]
print(dp[0])