from itertools import combinations
def solution(numbers):
    combi = combinations(numbers,2)
    result = []
    for (a,b) in combi:
        if (a+b) not in result:
            result.append(a+b)
    print(sorted(result))


solution([2,1,3,4,1])
