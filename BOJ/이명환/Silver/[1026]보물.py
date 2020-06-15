# import sys
# from itertools import permutations
# n = int(sys.stdin.readline())
# arr_A = list(map(int,sys.stdin.readline().split()))
# arr_B = list(map(int,sys.stdin.readline().split()))
# arr_A_per = list(permutations(arr_A))
# flag = True
# min = 0
# for i in arr_A_per:
#     temp = 0
#     for a,b in zip(i,arr_B):
#         temp += a*b
#     if flag:
#         min = temp
#         flag = False
#     else:
#         if temp < min:
#             min = temp
# print(min)
#본문에 맞게 A 배열만 바꿔서 문제를 풀려했는데 시간초과가 뜬다..
#재배열 부등식 hint 를 봤는데 내일 자료를 한번 보고 풀어 봐야겠다

import sys
n = int(sys.stdin.readline())
arr_A = sorted(list(map(int,sys.stdin.readline().split())))
arr_B = sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
min = 0
for a,b in zip(arr_A,arr_B):
    min += a*b
print(min)

#음.. 찜찜하다