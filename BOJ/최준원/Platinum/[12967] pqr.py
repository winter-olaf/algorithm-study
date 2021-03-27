# Memory Exceed
# 아니 이거는 파이썬으로 못푼다.
# 배열 크기가 최대 1억이므로 조합을 구하면 메모리 터짐
# from sys import stdin
# from itertools import combinations
# N, K = map(int, stdin.readline().split())
# arr = list(map(int, stdin.readline().split()))
#
# perm = list(combinations(range(N), 3))
# result = 0
# for p, q, r in perm:
#     if not (arr[p] * arr[q] * arr[r])%K:
#         result += 1
# print(result)

# prefix sum
from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)
N, K = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

selected = [0] * 3
result = 0

def pqr(idx, cnt, selected):
    global result

    if cnt == 3:
        tmp = 1
        for s_idx in selected:
            tmp *= arr[s_idx]
        if tmp%K == 0:
            result += 1
        return

    # idx가 index 끝까지 왔다면 break
    if idx == N:
        return

    selected[cnt] = idx
    pqr(idx+1, cnt+1, selected)
    pqr(idx+1, cnt, selected)

pqr(0, 0, selected)
print(result)