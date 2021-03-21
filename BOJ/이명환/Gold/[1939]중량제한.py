# import sys
# from collections import deque
#
# N,M = map(int,sys.stdin.readline().split())
# road = [[0 for i in range(N+1)] for j in range(N+1)]
# max_weight = 0
#
#
# for i in range(M):
#     a,b,c = map(int,sys.stdin.readline().split())
#     road[a][b] = c
#     road[b][a] = c
#
# factory1, factory2 = map(int,sys.stdin.readline().split())
# way = deque([[factory1,1000000000,[factory1]]])
#
# while(way):
#     bundle = way.popleft()
#     start = bundle[0]
#     weight = bundle[1]
#     passed = bundle[2]
#
#     if start == factory2:
#         if max_weight < weight:
#             max_weight = weight
#         continue
#     for i in range(1,N+1):
#         if road[start][i] and i not in passed:
#             if road[start][i] < weight:
#                 way.append([i, road[start][i], passed + [start]])
#             else:
#                 way.append([i,weight,passed + [start]])
#
#
# print(max_weight)

#시간초과 나올 것 같은데 > 시간초과는 안나오고 메모리 초과가 나왔다
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
road = [[] for j in range(n+1)]

for _ in range(m):
    y,x,w = map(int,sys.stdin.readline().split())
    road[y].append((x,w))
    road[x].append((y,w))

start,end = map(int,sys.stdin.readline().split())

_min,_max = 1,1000000000

def bfs(c):
    queue = deque()
    queue.append(start)
    passed = set()
    passed.add(start)
    result = []
    while queue:
        y = queue.popleft()
        for x,w in road[y]:
            if x not in passed and w>=c:
                passed.add(x)
                queue.append(x)
    return True if end in passed else False

result = _min
while _min <= _max:
    mid = (_min + _max)//2

    if bfs(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid -1
print(result)