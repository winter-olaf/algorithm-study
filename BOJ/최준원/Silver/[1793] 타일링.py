# 점화식 : (n-2)*2 + (n-1)
# n-2에서 2 X 1 크기의 타일을 세로로 쭉 늘어놓는 것은 n-1에 포함되어 있기 때문에 고려하지 않는다.

# memoization
# 0,1,2를 미리 넣어준다.
memo = [1,1,3]

def dp(n):
    if n >= 3 and len(memo) <= n:
        memo.append(dp(n-1) + dp(n-2)*2)
    return memo[n]

while 1:
    try:
        print(dp(int(input())))
    except:
        break