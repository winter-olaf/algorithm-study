# import sys
# from collections import deque
# testcase = int(sys.stdin.readline())
# for i in range(testcase):
#     funtions = sys.stdin.readline().split()
#     n = int(sys.stdin.readline())
#     arr = sys.stdin.readline().rstrip('\n')
#     arr_ac = []
#     temp = ''
#     error = False
#     for j in arr:
#         if (j != '[' and j != ',' and j != ']'):
#             temp += j
#         elif j == ',' or j == ']' and temp != '':
#             arr_ac.append(int(temp))
#             temp = ''
#     arr_deque = deque(arr_ac)
#     for k in funtions[0]:
#         if k == 'R':
#             arr_deque.reverse()
#         else:
#             if list(arr_deque) != []:
#                 arr_deque.popleft()
#             else:
#                 error = True
#     if error == True:
#         print('error')
#     else:
#         print(list(arr_deque))
# 시간초과

# import sys
# from collections import deque
# testcase = int(sys.stdin.readline())
# for i in range(testcase):
#     funtions = sys.stdin.readline().split()
#     n = int(sys.stdin.readline())
#     arr = sys.stdin.readline().rstrip('\n').lstrip('[')
#     error = False
#     arr_deque = deque() # 그냥 덱에 바로 원소 하나씩 추가
#     temp = ''
#     for j in arr:
#         if (j != ',' and j != ']'):
#             temp += j
#         elif j == ',' or j == ']' and temp != '':
#             arr_deque.append(int(temp))
#             temp = ''
#     for k in funtions[0]:
#         if k == 'R':
#             arr_deque.reverse()
#         else:
#             if arr_deque: # deque이 empty 한지 확인하려면 이렇게만 해도 된다.
#                 arr_deque.popleft()
#             else:
#                 error = True
#                 break # 시간효율을 위해 걍 바로 나가자
#     if error : # 요것도 혹시나해서..
#         print('error')
#     else:
#         print(list(arr_deque))
#시간초과 좀 찾아보니까 reverse가 시간을 엄청 잡아 먹는다고 한다..
import sys
from collections import deque
testcase = int(sys.stdin.readline())
for i in range(testcase):
    funtions = sys.stdin.readline().split()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip('\n').lstrip('[')
    error = False
    arr_deque = deque() # 그냥 덱에 바로 원소 하나씩 추가
    temp = ''
    for j in arr:
        if (j != ',' and j != ']'):
            temp += j
        elif j == ',' or j == ']' and temp != '':
            arr_deque.append(int(temp))
            temp = ''
    reverse = False # 뒤집을 경우인 flag를 만들었다
    for k in funtions[0]:
        if k == 'R':
            reverse = not reverse
        else:
            if arr_deque:
                if reverse:
                    arr_deque.pop()
                else:
                    arr_deque.popleft()
            else:
                error = True
                break
    if error :
        print('error')
    else:
        if reverse:
            arr_deque.reverse()
            arr_deque = list(arr_deque)
            arr_deque = ",".join([str(_) for _ in arr_deque])
            print('[',arr_deque,']',sep='')
        else:
            arr_deque = list(arr_deque)
            arr_deque = ",".join([str(_) for _ in arr_deque])
            print('[',arr_deque,']',sep='')
#출력에서도 헤맸다.. 그냥 출력하면 [1, 2, 3,...] 이렇게 중간중간 공백이 들어가서 틀렸다고 뜬 것이였다.