# 100/100
def solution(prices):
    lp = len(prices)
    result = [0]*lp

    for i in range(lp-1):
        for j in range(i,lp-1):
            if prices[i] <= prices[j]:
                result[i]+=1
            else:
                break # break를 써야 맞고 pass는 아님
    return result

# 100/100 ?!
def solution(prices):
    lp = len(prices)
    result = [0]*lp

    for i in range(lp-1):
        for j in range(i, lp-1):
            if prices[i] > prices[j]:
                break
            else:
                result[i]+=1
    return result

print(solution([1,2,3,2,3]))
