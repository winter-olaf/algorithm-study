import sys

a,b = map(int,input().split())
chess = []
for i in range(a):
    tmp = [sys.stdin.readlines() for x in range(b)]
    chess.append(tmp)
print(chess)