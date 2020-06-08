# import sys
# arr = list(sys.stdin.readline().rstrip('\n'))
# n = int(sys.stdin.readline())
# cursor = len(arr)
# for i in range(n):
#     instruct = sys.stdin.readline().split()
#     if instruct[0] == 'L':
#         if cursor != 0:
#             cursor -=1
#     elif instruct[0] == 'D':
#         if cursor == len(arr):
#             pass
#         else:
#             cursor +=1
#     elif instruct[0] == 'B':
#         if cursor == 0:
#             pass
#         elif cursor ==1:
#             arr = arr[1:]
#             cursor -=1
#         elif cursor ==2:
#             arr = arr[:cursor-1] + arr[2:]
#             cursor -=1
#         elif cursor >2:
#             arr = arr[:cursor - 1] + arr[cursor:-1]
#             cursor -= 1
#     elif instruct[0] == 'P':
#         if cursor == 0:
#             arr = list(instruct[1])+ arr[cursor:]
#             cursor+=1
#         else:
#             arr = arr[:cursor] + list(instruct[1]) + arr[cursor:]
#             cursor +=1
# arr = ('').join(arr)
# print(arr)
#테스트 케이스는 다 맞는데 시간초과
#문자 슬라이싱은 시간이 오래걸리는듯:??.. 다른방법을 공구하자

import sys
l_stack = list(sys.stdin.readline().rstrip('\n'))
n = int(sys.stdin.readline())
r_stack = []
for i in range(n):
    instruct = sys.stdin.readline().split()
    if instruct[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif instruct[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif instruct[0] == 'B' and l_stack:
        l_stack.pop()
    elif instruct[0] == 'P':
        l_stack.append(instruct[1])
print(''.join(l_stack + r_stack[::-1]))
#이걸를..

















