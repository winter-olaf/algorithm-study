import sys

a,b = map(int,input().split())
# chess_board = []
# for i in range(a):
#     chess_board.append(list(sys.stdin.readline().rstrip('\n')))
chess_board = [list(sys.stdin.readline().rstrip('\n')) for i in range(a)]
# print(chess_board) 

# 행과 열에서 각각 8을 뺀 수까지 시작 위치를 늘려가면서 최소값을 넣어야 함
# 문제에 명시된 대로 [0][0]의 값이 W,B인 두 가지의 경우만 고려하면 된다
def chess_check(arr):
    changes = []
    change = 0
    for x in range(a-7):
        for y in range(b-7):
            # B인 경우에는 짝수번째 인덱스 행(0,2,4,6)의 짝수번째 인덱스 원소가 B, 홀수는 W : 홀수번째 행의 짝수 원소가 W, 홀수는 B여야 함
            if arr[0][0] == 'B':
                
            
            # W인 경우에는 짝수번째 인덱스 행은 
            if arr[0][0] == 'W':
            

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
