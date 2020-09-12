# import sys
# from collections import deque
#
# t = int(sys.stdin.readline())
# for i in range(t):
#     group = 0
#     ans = 0
#     n = int(sys.stdin.readline())
#     student = list(map(int,sys.stdin.readline().split()))
#     student.insert(0,0)
#
#     visit = [0 for _ in range (n+1)]
#     student_deque = deque(student)
#     idx = n
#     first_node = False
#     while student_deque:
#         node = student_deque.pop()
#         if first_node == node:
#             ans += group
#             first_node = False
#             idx = len(student_deque) -1
#             group = 0
#             continue
#         if first_node == False:
#             first_node = idx
#         if visit[node] == 1:
#             first_node = False
#             idx = len(student_deque) -1
#             group = 0
#             continue
#         if node == idx:
#             ans +=1
#             first_node = False
#             idx = len(student_deque) -1
#             continue
#         group +=1
#         visit[node] = 1
#         student_deque.append(student[node])
#         idx = node
#     print(n-ans)

#대폭개선 필요할듯 설계를 좀 잘못한 느낌쓰..
import sys
sys.setrecursionlimit(999999)

def DFS(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = students[x]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        DFS(number)

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    students = [0] + list(map(int,sys.stdin.readline().split()))
    visited = [True] + [False] *n
    result = []

    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            DFS(i)
    print(n - len(result))