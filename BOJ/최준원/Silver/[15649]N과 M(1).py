# DFS
n, m = map(int,input().split())
visited = [False]*n
res = []

def dfs(count):
    if count==m:
        print(*res)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res.append(i+1)
            dfs(count+1)
            res.pop()
            visited[i] = False
dfs(0)
            

# permutations
'''
from itertools import permutations
n, m = map(int,input().split())
result = permutations([x for x in range(1,n+1)], m)
for i in result:
    print(' '.join(map(str, i)))
'''