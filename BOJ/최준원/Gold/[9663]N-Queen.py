# Back Tracking
# 1) N개의 퀸이 N X N 크기의 체스판에 놓여야 하니 한 행마다 무적권 한개씩 존재해야 함
# 2) 0열부터 N-1열까지 퀸을 놓는 for문 돌리기
# 3) 유망한지(놓을 킹능성 있는지) 검사하는 함수를 돌려준다.
from sys import stdin
n = int(stdin.readline())
row = [0] * n
result = 0

# 유망한가?
def ganeung(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == (x-i):
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if ganeung(x):
                dfs(x+1)
dfs(0)
print(result)