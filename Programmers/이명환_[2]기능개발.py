# import operator
#
# def solution(progresses, speeds):
#     answer = []
#     while(True):
#         temp = 0
#         if progresses ==[]:
#             break
#         while(True):
#             if progresses[0] >= 100:
#                 break
#             progresses = list(map(operator.add,progresses,speeds))
#
#         for i in progresses:
#             if i >=100:
#                 temp +=1
#         for k in range(temp):
#             progresses.pop(0)
#         answer.append(temp)
#     return answer
# 채점 결과
# 정확성: 30.0
# 합계: 30.0 / 100.0

import operator

def solution(progresses, speeds):
    answer = []
    while(True):
        temp = 0
        if progresses ==[]:
            break
        while(True):
            if progresses[0] >= 100:
                break
            progresses = list(map(operator.add,progresses,speeds))

        for i in progresses:
            if i >=100:
                temp +=1
            else:
                break
        for k in range(temp):
            progresses.pop(0)
            speeds.pop(0)
        answer.append(temp)
    return answer