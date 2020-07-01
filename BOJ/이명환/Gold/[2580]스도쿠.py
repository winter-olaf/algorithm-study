import sys

board = [list(map(int,sys.stdin.readline().split())) for i in range(9)]
def check(board,r,c):
    possible_num = [i for i in range(1,10)]
    impossible_num = []
    for i in range(1,10):
        if i in board[r]:
            impossible_num.append(i)
    for i in range(9):
        k = board[i][c]
        if k in [1,2,3,4,5,6,7,8,10]:
            impossible_num.append(k)
    possible_num = set(possible_num) -set(impossible_num)
    return possible_num

def fill_num(board,r,c):
    if c == 9:
        r +=1
        c = 0
    if r == 9:
        print(board)
        sys.exit()
    if board[r][c] == 0:
        possible_num = check(board, r, c)
        if possible_num == set():
            return False
        for i in possible_num:
            board[r][c] = i
            fill_num(board, r, c+1)
    else:
        c += 1
        if c == 9:
            r += 1
            c = 0
        fill_num(board, r, c)
fill_num(board,0,0)
##츌력이 문제네 ㄹㅇㅋㅋ