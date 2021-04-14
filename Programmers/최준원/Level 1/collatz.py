def solution(num):
    cnt = 0
    while cnt < 500:
        if num == 1:
            return cnt
        if num%2:
            num = num*3+1
        else:
            num//=2
        cnt+=1
    return -1

print(solution(6))
print(solution(16))
print(solution(626331))