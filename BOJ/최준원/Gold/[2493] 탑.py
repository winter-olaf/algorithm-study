from sys import stdin
n = int(input())
towers = list(map(int, stdin.readline().split()))

stack = []
result = []

# 뒤에서부터 봐야 편하다
i = n - 1
while i > 0:
    if towers[i]



'''tc
5
6 9 5 7 4
'''
