# DFS
# dfs를 재귀적으로 돌린다. n중 포문이되 완전탐색이 아니라고 생각하면 된다. 순열의 경우는 완전탐색에 근접하지만 다른 제약조건이 있는 문제의 경우 시간복잡도가 더욱 줄어든다.
n, m = map(int,input().split())
visited = [False]*n
res = []

def dfs(count):
    if count==m: 
        return
    for i in range(n): # n번만큼 반복 (if n == 4, 1,2,3,4 = 4번 반복)
        # count = 0으로 시작, visited의 상태는 False, False, False, False
        if not visited[i]: # visited가 False이면
            visited[i] = True # 방문했다는 의미로 visited는 True로 변경해둔다. 1을 방문하고 난 뒤 2를 방문한다면 True, True, False, False 상태이다.
            # print(visited) # 여기서 visited의 상태를 찍어 보면 이해가 쉽다.
            res.append(i+1) # result에 1이 하나 쌓인다.
            dfs(count+1) # recursive하게 dfs. count = 1이 된 상태로 한번 더 돈다. 이때 visited[0]은 True이기 때문에, 2,3,4만 for문으로 한번 더 돌게 된다.
            # 모든 작업이 끝나고 2개의 순열이 결과 배열에 append 된 뒤, return된 dfs. 이제 다음 작업을 위해 
            res.pop() # 1,2가 되었다면 2를 pop하고 visited[1] 값을 다시 False로 바꾸어 준다. 다음으로 3을 추가하고, 4를 추가하는 작업이 반복된다.
            visited[i] = False # visited에 해당 인덱스 값을 False로 바꾸어 준다.
dfs(0)
'''
[True, False, False, False]
[True, True, False, False]
[True, False, True, False]
[True, False, False, True]
[False, True, False, False]
[True, True, False, False]
[False, True, True, False]
[False, True, False, True]
[False, False, True, False]
[True, False, True, False]
[False, True, True, False]
[False, False, True, True]
[False, False, False, True]
[True, False, False, True]
[False, True, False, True]
[False, False, True, True]
'''
# permutations
'''
from itertools import permutations
n, m = map(int,input().split())
result = permutations([x for x in range(1,n+1)], m)
for i in result:
    print(' '.join(map(str, i)))
'''
