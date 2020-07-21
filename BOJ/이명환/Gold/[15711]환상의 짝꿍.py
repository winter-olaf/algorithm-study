# import sys
#
# testcase = int(sys.stdin.readline())
#
# def is_prime(x):
#     if x <2:
#         return False
#     if x in (2,3):
#         return True
#     if x%2 == 0 or x%3 == 0:
#         return False
#     if x < 9:
#         return True
#     k,l=5, x**0.5
#     while k<=l:
#         if x%k == 0 or x %(k+2) == 0:
#             return False
#         k+=6
#     return True
#
# for t in range(testcase):
#     strap = list(map(int,sys.stdin.readline().split()))
#     A = strap[0]
#     B = strap[1]
#     C = A+B
#     alpha =2
#     flag = False
#     while(alpha<=C):
#         if is_prime(alpha):
#             beta = C - alpha
#             if is_prime(beta):
#                 flag = True
#                 break
#         alpha+=1
#     if flag:
#         print('YES')
#     else:
#         print('NO')
#  시간초과

import sys

testcase = int(sys.stdin.readline())

def is_prime(x):
    if x <2:
        return False
    if x in (2,3):
        return True
    if x%2 == 0 or x%3 == 0:
        return False
    if x < 9:
        return True
    k,l=5, x**0.5
    while k<=l:
        if x%k == 0 or x %(k+2) == 0:
            return False
        k+=6
    return True

for t in range(testcase):
    strap = list(map(int,sys.stdin.readline().split()))
    A = strap[0]
    B = strap[1]
    C = A+B
    flag = False
    if C >= 4:
        if C%2 == 0:
            flag = True
        else:
            if is_prime(C-2):
                flag = True

    if flag:
        print('YES')
    else:
        print('NO')
# https://algwang.tistory.com/57