def solution(n):
    list_n = [i for i in range(1,n+1)]
    result = 0
    cnt = 0
    while(True):
        result = 0
        if list_n == []:
            break
        for k in list_n:
            result += k
            if result == n:
                cnt+=1
                list_n.pop(0)
                break
            elif result > n:
                list_n.pop(0)
                break
    return cnt

print(solution(15))