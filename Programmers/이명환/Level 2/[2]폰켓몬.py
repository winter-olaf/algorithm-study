# from itertools import combinations
#
# def solution(nums):
#     n = int(len(nums)/2)
#     num_combi = set(list(combinations(nums, n)))
#     answer = 0
#     for i in num_combi:
#         if len(set(i)) > answer:
#             answer = len(set(i))
#     return answer
# 채점 결과
# 정확성: 30.0
# 합계: 30.0 / 100.0
# 시간초과로 틀림

# from itertools import combinations
#
# def solution(nums):
#     n = int(len(nums)/2)
#     if len(set(nums))>= n:
#         answer = n
#         return answer
#     num_combi = set(list(combinations(nums, n)))
#     answer = 0
#     for i in num_combi:
#         if len(set(i)) > answer:
#             answer = len(set(i))
#     return answer

# 채점 결과
# 정확성: 50.0
# 합계: 50.0 / 100.0

from itertools import combinations

def solution(nums):
    n = int(len(nums)/2)
    if len(set(nums))>= n:
        answer = n
        return answer
    else:
        answer = len(set(nums))
        return answer
#개 낚시에 걸린느낌쓰