# import sys
#
#
# n = int(sys.stdin.readline())
# numbers = []
#
#
# def pushitem(list,num):
#     if(list ==[]):
#         list.append(num)
#     else:
#         list_len = len(list)
#         for i in range(list_len):
#             if list[i] >= num:
#                 list.insert(i, num)
#                 break
#         if list_len == len(list):
#             list.append(num)
#
# for i in range(1,n+1):
#     pushitem(numbers, int(sys.stdin.readline()))
#     if(i%2 == 1):
#         print(numbers[int(i/2)])
#     else:
#         print(min(numbers[int(i/2)],numbers[int(i/2)-1]))
#역시 시간초과

import sys
import heapq

n = int(sys.stdin.readline())
left, right = [],[]

for i in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left,(-num,num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1]> right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right,(left_value,left_value))
        heapq.heappush(left, (-right_value, right_value))
    print(left[0][1])
