# import sys

# # 문제에 명시된 대로 [0][0]의 값이 W,B인 두 가지의 경우만 고려하면 된다
# def chess_check(arr):
#     change = 0
#     # B인 경우에는 짝수번째 인덱스 행(0,2,4,6)의 짝수번째 인덱스 원소가 B, 홀수는 W - 홀수번째 행의 짝수 원소가 W, 홀수는 B여야 함. 그러므로 위의 예와 다른 경우 change 변수를 +1한다.
#     if arr[0][0] == 'B':
#         for x in range(8):
#             for y in range(8):
#                 if x in [0,2,4,6]:
#                     if y in [0,2,4,6] and arr[x][y] == 'W':
#                         change+=1
#                     elif y in [1,3,5,7] and arr[x][y] == 'B':
#                         change+=1
#                 elif x in [1,3,5,7]:
#                     if y in [1,3,5,7] and arr[x][y] == 'W':
#                         change+=1
#                     elif y in [0,2,4,6] and arr[x][y] == 'B':
#                         change+=1
#     # W인 경우에는 반대로 하면 된다                        
#     if arr[0][0] == 'W':
#         for x in range(8):
#             for y in range(8):
#                 if x in [0,2,4,6]:
#                     if y in [0,2,4,6] and arr[x][y] == 'B':
#                         change+=1
#                     elif y in [1,3,5,7] and arr[x][y] == 'W':
#                         change+=1
#                 elif x in [1,3,5,7]:
#                     if y in [1,3,5,7] and arr[x][y] == 'B':
#                         change+=1
#                     elif y in [0,2,4,6] and arr[x][y] == 'W':
#                         change+=1
#     return change
        

# # 행과 열에서 각각 8을 뺀 수까지 시작 위치를 늘려가면서 최소값을 넣어야 함
# a,b = map(int,input().split())
# # chess_board = []
# # for i in range(a):
# #     chess_board.append(list(sys.stdin.readline().rstrip('\n')))
# chess_board = [list(sys.stdin.readline().rstrip('\n')) for i in range(a)]
# # print(chess_check(chess_board))

# result = []
# for x in range(a-7):
#     for y in range(b-7):
#         arr = [i[(0+y):(8+y)] for i in chess_board[(0+x):(8+x)]]
#         # arr = [i[(0+x):(8+x)] for i in chess_board[(0+y):(8+y)]] 실수
#         result.append(chess_check(arr))
#         # for i in arr:
#         #     print(i)
#         # print("---------")
# print(min(result))
        

'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
'''
# 주석제거 ?? 이게 왜 안되지?
# import sys
# def chess_check(arr):
#     change = 0
#     if arr[0][0] == 'B':
#         for x in range(8):
#             for y in range(8):
#                 if x in [0,2,4,6]:
#                     if y in [0,2,4,6] and arr[x][y] == 'W':
#                         change+=1
#                     elif y in [1,3,5,7] and arr[x][y] == 'B':
#                         change+=1
#                 elif x in [1,3,5,7]:
#                     if y in [1,3,5,7] and arr[x][y] == 'W':
#                         change+=1
#                     elif y in [0,2,4,6] and arr[x][y] == 'B':
#                         change+=1 
#     if arr[0][0] == 'W':
#         for x in range(8):
#             for y in range(8):
#                 if x in [0,2,4,6]:
#                     if y in [0,2,4,6] and arr[x][y] == 'B':
#                         change+=1
#                     elif y in [1,3,5,7] and arr[x][y] == 'W':
#                         change+=1
#                 elif x in [1,3,5,7]:
#                     if y in [1,3,5,7] and arr[x][y] == 'B':
#                         change+=1
#                     elif y in [0,2,4,6] and arr[x][y] == 'W':
#                         change+=1
#     return change

# 음, 각각의 경우를 구해서 둘의 최소값을 따져 줘야 할 듯 하다. 
# 되겠냐? 바보같은 생각을 하네;;
# import sys
# def chess_check(arr):
#     bchange = 0
#     wchange = 0
#     if arr[0][0] == 'B':
#         for x in range(8):
#             for y in range(8):
#                 if x in [0,2,4,6]:
#                     if y in [0,2,4,6] and arr[x][y] == 'W':
#                         bchange+=1
#                     elif y in [1,3,5,7] and arr[x][y] == 'B':
#                         bchange+=1
#                 elif x in [1,3,5,7]:
#                     if y in [1,3,5,7] and arr[x][y] == 'W':
#                         bchange+=1
#                     elif y in [0,2,4,6] and arr[x][y] == 'B':
#                         bchange+=1 
#     if arr[0][0] == 'W':
#         for x in range(8):
#             for y in range(8):
#                 if x in [0,2,4,6]:
#                     if y in [0,2,4,6] and arr[x][y] == 'B':
#                         wchange+=1
#                     elif y in [1,3,5,7] and arr[x][y] == 'W':
#                         wchange+=1
#                 elif x in [1,3,5,7]:
#                     if y in [1,3,5,7] and arr[x][y] == 'B':
#                         wchange+=1
#                     elif y in [0,2,4,6] and arr[x][y] == 'W':
#                         wchange+=1

# 되겠냐가 아니라 된다!! [0][0]값을 제한하면 당연히 한쪽은 0000000만 나오지.
# 맨 앞이 W이든 B이든 각 경우를 모두 시험해 봐야 하는데 if를 쓰면 안되지 멍청아;;
# 맨 앞이 B로 시작했더라도 뒤에가 싹 WB순인 경우에는 그냥 B를 W로 바꾸는게 제일 빠른 것이다.
# WB순 - BW순 각자의 경우를 생각한 2중 for문을 돌리면 된다

# 정답!
import sys
def chess_check(arr):
    bchange = 0
    wchange = 0
    for x in range(8):
        for y in range(8):
            if x in [0,2,4,6]:
                if y in [0,2,4,6] and arr[x][y] == 'W':
                    bchange+=1
                elif y in [1,3,5,7] and arr[x][y] == 'B':
                    bchange+=1
            elif x in [1,3,5,7]:
                if y in [1,3,5,7] and arr[x][y] == 'W':
                    bchange+=1
                elif y in [0,2,4,6] and arr[x][y] == 'B':
                    bchange+=1 
    for x in range(8):
        for y in range(8):
            if x in [0,2,4,6]:
                if y in [0,2,4,6] and arr[x][y] == 'B':
                    wchange+=1
                elif y in [1,3,5,7] and arr[x][y] == 'W':
                    wchange+=1
            elif x in [1,3,5,7]:
                if y in [1,3,5,7] and arr[x][y] == 'B':
                    wchange+=1
                elif y in [0,2,4,6] and arr[x][y] == 'W':
                    wchange+=1
    return min(bchange,wchange)

a,b = map(int,input().split())
chess_board = [list(sys.stdin.readline().rstrip()) for i in range(a)]
result = []
for x in range(a-7):
    for y in range(b-7):
        arr = [i[(0+y):(8+y)] for i in chess_board[(0+x):(8+x)]]
        result.append(chess_check(arr))
print(min(result))