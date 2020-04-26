def solution(n):
    li = [0,1,0]
    for i in range(n):
        li[2] = li[0] +li[1]
        li.append(li.pop(0))
    answer = li[0]%1234567
    return answer

solution(5)