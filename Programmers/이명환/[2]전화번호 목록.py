from collections import Counter

def solution(clothes):
    each_possible = Counter([i for _, i in clothes])
    all_possible = 1 
    for key in each_possible:
        all_possible *= (each_possible[key]+1)

    answer = all_possible-1
    return answer