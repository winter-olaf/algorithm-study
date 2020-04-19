def solution(A,B):
    A.sort(reverse = True)
    B.sort()
    result = 0
    for i,j in zip(A,B):
        result += i*j
    return reuslt

# 다른사람 풀이
# def getMinSum(A,B):
#     return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
