import sys
answer = 0
N,M,V = map(int,sys.stdin.readline().split())
matrix = [[0]*(N + 1)for _ in range(N+1)]
for i in range(M):
    temp1,temp2 = map(int,sys.stdin.readline().split())
    matrix[temp1][temp2] = 1
    matrix[temp2][temp1] = 1
# DFS(깊이 우선 탐색)
def DFS(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = DFS(search_node,row,foot_prints)
    return foot_prints

# BFS(너비 우선 탐색)
def BFS(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints

print(*DFS(V,matrix,[]))
print(*BFS(V))