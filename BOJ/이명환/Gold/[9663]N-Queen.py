# 윗줄에 나와 겹치는 퀸이 있는지 확인
# def adjacent(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
#             return False
#     return True
#
#
# # 한줄씩 재귀하며 DFS를 실행
# def dfs(x):
#     global result
#
#     if x == N:
#         result += 1
#
#     else:
#         for i in range(N):
#             row[x] = i
#             if adjacent(x):
#                 dfs(x + 1)
#
#
# N = int(input())
# row = [0] * N
# result = 0
# dfs(0)
# print(result)
# 시간초과

n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            #모두가 False 일 때
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)

#pypy3제출
# 출처: https://rebas.kr/761 [PROJECT REBAS]