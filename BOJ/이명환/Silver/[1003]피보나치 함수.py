# import sys
# T = int(sys.stdin.readline())
# global cntZero
# cntZero = 0
# global cntOne
# cntOne = 0
# def fibonacci(n):
#     global cntZero
#     global cntOne
#     if n == 0 :
#         cntZero +=1
#         return 0
#     elif n ==1:
#         cntOne +=1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for i in range(T):
#     N = int(sys.stdin.readline())
#     fibonacci(N)
#     print(cntZero,cntOne)
#     cntOne =0
#     cntZero = 0

# 아마 시간제한 0.25라 시간제한 걸리듯?

import sys
T = int(sys.stdin.readline())
cntOne = 0
cntZero = 1
temp = 0

for i in range(T):
    N = int(sys.stdin.readline())
    while(True):
        if N == 0:
            break
        temp = cntZero
        cntZero = cntOne
        cntOne = temp + cntZero
        N-=1

    print(cntZero,cntOne)
    cntOne = 0
    cntZero = 1
    temp = 0