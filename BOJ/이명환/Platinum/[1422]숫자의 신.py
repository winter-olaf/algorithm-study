# import sys
#
# K,N = map(int,sys.stdin.readline().split())
# numbers = []
# combine = []
# max_ciper = 0
# answer = ''
#
# for i in range(K):
#     numbers.append(int(sys.stdin.readline()))
#
# def push_num(num,cipher):
#     is_pushed =False
#     if combine:
#         for index,i in enumerate(combine):
#             c_num, c_cipher = i
#             if(c_cipher == cipher):
#                 if(num>=c_num):
#                     combine.insert(index, (num, cipher))
#                     is_pushed = True
#                     break
#             elif(c_cipher > cipher):
#                 c_num_cut = int(str(c_num)[0:cipher])
#                 if(num>=c_num_cut):
#                     combine.insert(index, (num, cipher))
#                     is_pushed = True
#                     break
#                     #998 9989 같은 경우를 처리 해줘야한다.
#             elif(c_cipher<cipher):
#                 num_cut = int(str(num)[0:c_cipher])
#                 if (num_cut > c_num):
#                     combine.insert(index, (num,cipher))
#                     is_pushed = True
#                     break
#         if not is_pushed:
#             combine.append((num,cipher))
#     else:
#         combine.append((num,cipher))
#
#
# for _ in range(N):
#     if numbers:
#         num = numbers.pop()
#         cipher = len(str(num))
#         if cipher>max_ciper: max_ciper=cipher
#         push_num(num,cipher)
#     else:
#         for index,i in enumerate(combine):
#             num, cipher = i
#             if cipher == max_ciper:
#                 combine.insert(index,(num,cipher))
#                 break
# for s in combine:
#     x = str(s[0])
#     answer +=x
# print(combine)
# print(answer)

import sys
from functools import cmp_to_key

k,n = map(int,sys.stdin.readline().split())
nums = []
for i in range(k):
    nums.append(int(sys.stdin.readline()))

max_num = max(nums)
for _ in range(n-len(nums)):
    nums.append(max_num)
nums = sorted(nums, key= cmp_to_key(lambda a,b: -1 if int(str(a)+str(b)) > int(str(b) +str(a)) else 1) )

print(*nums,sep='')