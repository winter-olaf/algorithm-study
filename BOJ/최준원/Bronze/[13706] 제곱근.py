# from sys import stdin
# N = int(stdin.readline())

# def root(N):
#     if N <= 2:
#         return
#     i = 2
#     while i <= N // i:
#         if N//i == i:
#             return i
#         i += 1
#
# print(root(N))

# def root(N):
#     # Binary Search
#     left = 1
#     right = N
#     mid = 0
#
#     while left < right:
#         mid = (left + right)//2
#         if mid == N // mid:
#             break
#         if mid < N // mid:
#             left += 1
#         elif mid > N // mid:
#             right = mid - 1
#     print(mid)
#
# root(N)

def root(N):
    right = N
    left = (right + 1) // 2

    while left < right:
        right = left
        left = (right + N // right) // 2
    print(right)

root(int(input()))

# import math
# # 이걸론 안되네..
# # print(math.isqrt(int(input())))
#
# print(int(math.sqrt(int(input()))))