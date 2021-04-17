N = int(input())
a, b = map(int, input().split())
M = int(input())
tree = [[] for x in range(N+1)]

for i in range(M):
    p, c = map(int, input().split())
    tree[c].append(p)
    tree[p].append(c)

res = -1

from collections import deque

def bfs(start):
    global res

    q = deque([(start, 0)])
    visited = [0]*(N+1)
    while q:
        cur, val = q.popleft()
        if cur == b:
            res = val
            return
        for i in tree[cur]:
            if not visited[i]:
                q.append((i, val+1))
                visited[i] = 1
bfs(a)
print(res)