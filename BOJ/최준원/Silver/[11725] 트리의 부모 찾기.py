# from collections import deque
# N = int(input())
#
# tree = [[] for x in range(N+1)]
# parent = [0] * (N+1)
#
# for i in range(N-1):
#     s, e = map(int, input().split())
#     tree[s].append(e)
#     tree[e].append(s)
#
# queue = deque([1])
# visit = [False] * (N+1)
#
# while queue:
#     root = queue.popleft()
#     for i in tree[root]:
#         if not visit[i]:
#             parent[i] = root
#             queue.append(i)
#             visit[i] = True
#
# for i in parent[2:]:
#     print(i)

import sys
sys.setrecursionlimit(10**9)

N = int(input())

tree = [[] for x in range(N+1)]
parent = [0] * (N+1)

for i in range(N-1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(node):
    for i in tree[node]:
        if not parent[i]:
            parent[i] = node
            dfs(i)

dfs(1)

for i in parent[2:]:
    print(i)