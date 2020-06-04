# M*N크기의 보드를 받아, row +1, colmn + 1 해가면서 최소 개수를 찾아야 할듯?
import sys
N_M = list(map(int,sys.stdin.readline().split()))
ans = 64
board = []
for i in range(N_M[0]):
    board.append(list(map(list,sys.stdin.readline().split())))
board = sum(board,[])

def check_min_chess(board,i,j):
    ans =0
    flag =1
    for y in range(8):
        if y != 0:
            if flag == 1:
                flag = 0
            else:
                flag =1
        for x in range(8):
            if flag == 1:
                if board[y+j][x+i] == 'B':
                    flag = 0
                    ans+=1
                else:
                    flag = 0
            else:
                if board[y+j][x+i] == 'W':
                    flag = 1
                    ans+=1
                else:
                    flag = 1
    min = ans
    ans = 0
    flag =0
    for y in range(8):
        if y != 0:
            if flag == 1:
                flag = 0
            else:
                flag =1
        for x in range(8):
            if flag == 1:
                if board[y+j][x+i] == 'B':
                    flag = 0
                    ans+=1
                else:
                    flag = 0
            else:
                if board[y+j][x+i] == 'W':
                    flag = 1
                    ans+=1
                else:
                    flag = 1
    if ans < min:
        return ans
    else:
        return min


for i in range(N_M[1]-7):
    for j in range(N_M[0]-7):
        k = check_min_chess(board, i, j)
        if ans >= k:
            ans = k
print(ans)
#개노가다로 풀었따.....
#20200606