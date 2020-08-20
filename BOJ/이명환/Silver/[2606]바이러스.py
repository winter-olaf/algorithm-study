# import sys
# from collections import deque
#
# computer = int(sys.stdin.readline())
# connectedComputer = int(sys.stdin.readline())
# network = []
# isConneted = [0 for _ in range(computer+1)]
# temp = []
# for _ in range(connectedComputer):
#     network.append(list(map(int,sys.stdin.readline().split())))
#
# network = sorted(network,key=lambda net: net[0])
# def virus():
#     isConneted[1] =1
#     q = deque(network)
#     while q:
#         i,j = q.popleft()
#         if isConneted[i] or isConneted[j]:
#            isConneted[i] =1
#            isConneted[j] =1
#         else:
#             temp.append([i,j])
#     for k in temp:
#         i,j = k
#         if isConneted[i] or isConneted[j]:
#             isConneted[i] = 1
#             isConneted[j] = 1
#         print(i,j)
#     print(sum(isConneted)-1)
# virus()
# #음..양방향으로 검사가 안되는듯.
import sys
computer = int(sys.stdin.readline())
connectedComputer = int(sys.stdin.readline())
virus_map = [[0 for _ in range(computer + 1)] for _ in range(computer + 1)]

# 2차원 배열 안에 넣어주기
for _ in range(connectedComputer):
    x, y = map(int, sys.stdin.readline().split())
    virus_map[x][y] = 1
    virus_map[y][x] = 1

# 1과 연결된 모든 노드 뽑기
def bfs(virus_map, start):
    queue = [start]
    visited = []

    while queue:
        temp = queue.pop(0)
        visited.append(temp)

        for i in range(len(virus_map)):
            if virus_map[temp][i] and i not in visited and i not in queue:
                queue.append(i)

    return len(visited) - 1


# 1을 제외한 감염된 노드 수 출력
print(bfs(virus_map, 1))
#2차원 배열을 써서 모든 노드를 탐색
