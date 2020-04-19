# Veeeeeeeeeeeeeeery EZ
def solution(a,b):
    a = sorted(a)
    b = sorted(b,reverse=True)
    return sum([a*b for a,b in zip(a,b)])

print(solution([1, 4, 2],[5, 4, 4]))