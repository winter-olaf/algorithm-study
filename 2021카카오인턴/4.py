from collections import deque
import copy

def solution(n, start, end, roads, traps):
    answer = 0
    adj1 = [[0]*(n+1) for x in range(n+1)]
    # 인접행렬
    for road in roads:
        s, e, w = road[0], road[1], road[2]
        adj1[s][e] = w

    adj2 = copy.deepcopy(adj1)
    # # 트랩 밟았을 때의 인접행렬
    # for road in roads:
    #     s, e, w = road[0], road[1], road[2]
    #     adj2[e][s] = w

    # 최단 거리 탐색
    Q = deque([(start,0,1)])

    while Q:
        cv, cd, cdj = Q.popleft()

        if cv == end:
            answer = cd
            break

        # reverse
        # cdj가 1이면 adj1, -1이면 adj2
        if cv in traps:
            cdj *= -1

            for i in range(1, n+1):
                if adj2[cv][i]:
                    adj2[i][cv] = adj2[cv][i]
                    adj2[cv][i] = 0

        print(adj1)

        if cdj == 1:
            for i in range(1, n+1):
                if adj1[cv][i]:
                    Q.append((i, cd + adj1[cv][i], cdj))
        else:
            for i in range(1, n+1):
                if adj2[cv][i]:
                    Q.append((i, cd + adj2[cv][i], cdj))

    return answer

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))