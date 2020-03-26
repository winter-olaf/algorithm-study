def solution(p,l):
    # enumerate를 사용하여 idx 위치를 정해 놓는다
    while True:
        if p = []:
            break
        
    maxP = p.index(max(p))
    p = sorted(p[maxP:],reverse=True)+sorted(p[:maxP],reverse=True)

    print(p)
    return (p.index(result))

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))