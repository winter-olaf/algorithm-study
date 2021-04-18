def solution(a, edges):
    answer = -1

    if sum(a) == 0:
        graph = [list() for x in range(len(a))]

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))