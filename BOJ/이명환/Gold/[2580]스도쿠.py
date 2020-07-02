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
        if k in [1,2,3,4,5,6,7,8,9,10]:
            impossible_num.append(k)
    r_s = (r // 3) * 3
    c_s = (c // 3) * 3
    for x in range(r_s, r_s+3):
        for y in range(c_s, c_s+3):
            if board[x][y] in [1,2,3,4,5,6,7,8,9,10]:
                impossible_num.append(board[x][y])
    if set(impossible_num) == [1,2,3,4,5,6,7,8]:
        return False
    possible_num = set(possible_num) -set(impossible_num)
    return possible_num

def fill_num(board,r,c):
    if c == 9:
        r += 1
        c = 0
    if r == 9:
        for x in range(9):
            for y in range(9):
                print(board[x][y], end=((" ", "\n")[y == 8]))
        sys.exit()
    while(board[r][c]!= 0):
        c += 1
        if c == 9:
            r += 1
            c = 0
        if r == 9:
            for x in range(9):
                for y in range(9):
                    print(board[x][y], end=((" ", "\n")[y == 8]))
            sys.exit()
    possible_num = check(board, r, c)
    if possible_num == False:
        return
    for i in possible_num:
        board[r][c] = i
        if (fill_num(board, r, c+1)):
            pass
        else:
            board[r][c] = 0
fill_num(board,0,0)
#pypy제출... 그냥 파이썬은 시간초과뜸. .