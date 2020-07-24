# import sys
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
# ss_range = list(map(int,sys.stdin.readline().split()))
# ss_min = ss_range[0]
# ss_max = ss_range[1]
#
# prime = 2
# x = 2
# answer = 0
# y = 1 #배수
# flag = False
# arr_list = []
#
# while(True):
#     if is_prime(prime):
#         while(True):
#             if y ==1 and (prime**x)*y > ss_max:
#                 flag = True
#                 break
#             if (prime**x)*y < ss_min:
#                 y +=1
#             elif (prime**x)*y > ss_max:
#                 y =1
#                 break
#             else:
#                 if (prime**x)*y in arr_list:
#                     y+=1
#                     pass
#                 else:
#                     arr_list.append((prime**x)*y)
#                     answer +=1
#                     y+=1
#     if flag == True:
#         break
#     prime+=1
# total = ss_max - ss_min +1
# answer = total - answer
# print(answer)
# #제곱수로 나누기 해서 되나안되나도 판별 해야할듯
# 시간초과

import sys
import math

results = []
min_num, max_num = map(int, sys.stdin.readline().split())
validation = [1 for _ in range(min_num, max_num+1)]

search_target = int(math.sqrt(max_num))
# max의 값보다 작은 모든 제곱수의 목록을 생성
squares = [v**2 for v in range(2, search_target+1)]
for square in squares:
    # min부터 max까지의 수 중, 해당 제곱수의 최소의 배수를 구함.
    cur_idx = (math.ceil(min_num / square) * square) - min_num
    while cur_idx <= max_num - min_num:
        # 제곱수의 배수인 경우 0으로 대체
        validation[cur_idx] = 0
        # 다음 제곱수의 index를 구함.
        cur_idx += square

# 남은 1들의 개수가 제곱 ㄴㄴ수의 개수가 된다.
result = sum(validation)
results.append(result)

for result in results:
    sys.stdout.write(str(result))
# https://nerogarret.tistory.com/32