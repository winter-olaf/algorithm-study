# def solution(people, limit):
#     import math
#     pivot = limit/2
#     big_li = []
#     small_li = []
#     ans = 0
#     for i in people:
#         if i > pivot:
#             big_li.append(i)
#         else:
#             small_li.append(i)
#     big_li.sort(reverse=True)
#     small_li.sort(reverse=True)
#     for i in big_li:
#         for j in small_li[:]:
#             if i+j <= limit:
#                 small_li.remove(j)
#                 ans+=1
#                 break
#     b = len(big_li)-ans
#     s = math.ceil((len(small_li) - ans)/2)
#     answer = ans + b + s
#     return answer
# 정확성: 20.0
# 효율성: 10.0
# 합계: 30.0 / 100.0
def solution(people, limit):
    people = sorted(people, reverse=True)
    big, small = (0, len(people) - 1)
    while big <= small:
        #무게의 여유가 있으면 뒤에사람도 함께 태움
        if people[big] + people[small] <= limit:
            small -= 1
        big += 1
    answer = big
    return answer