def factor(num):
    i = 1
    res = 1
    while i <= num // 2:
        if not num%i:
            res += 1
        i += 1
    return res

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if factor(i)%2:
            answer -= i
        else:
            answer += i

    return answer