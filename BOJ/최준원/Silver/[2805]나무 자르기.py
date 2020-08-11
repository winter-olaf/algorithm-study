from sys import stdin
N, M = map(int,stdin.readline().split())
trees = list(map(int,stdin.readline().split()))
T = 0
trees.sort()
# mid = lIdx//rIdx
while T != M:
    if 