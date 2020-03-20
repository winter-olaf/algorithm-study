def solution(prices):
    answer = []
    for idx,i in enumerate(prices):
        cnt = 0
        while(True):
            idx += 1
            if idx == len(prices):
                answer.append(cnt)
                break
            if i > prices[idx]:
                cnt += 1
                answer.append(cnt)
                break
            cnt += 1
    return answer

print(solution([1,2,3,2,3]))