def solution(N, stages):
    answer = []
    cnt = len(stages)

    for i in range(1, N+1):
        challenger = stages.count(i)
        if cnt == 0:
            answer.append((i, 0))
        else:
            answer.append((i, challenger/cnt))
        cnt -= challenger
    result = sorted(answer, key=lambda x:x[1], reverse=True)

    return [x[0] for x in result]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(5,  [2,1,2,4,2,4,3,3]))
print(solution(8,  [1,2,3,4,5,6,7]))