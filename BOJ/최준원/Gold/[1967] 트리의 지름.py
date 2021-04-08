from sys import setrecursionlimit, stdin
N = int(stdin.readline())
tree = [[] for x in range(N+1)]

for _ in range(N-1):
    s, e, v = map(int, stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)
