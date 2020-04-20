# 단순하게 풀어보고 가볍게 실패!
# 13.3/100
# def solution(stock, dates, supplies, k):
#     result = 0
#     # 공급용 변수
#     cnt = 0

#     while True:
#         # 매일 재고와 날짜를 하나씩 제거
#         k -= 1
#         stock -= 1
#         if k == 0:
#             break
#         # 재고가 날짜보다 많거나 같으면 break
#         if stock >= k:
#             break
#         # 재고가 다 떨어지면
#         if stock < 0:
#             stock += supplies[cnt]
#             result += 1
#             cnt += 1

#     return result


# 효율성 issue라는 것을 염두하고 풀이
# 어려워서 구글을 참고함. max-heap의 구성에서 -1번째를 pop하는 이유를 아직 잘 모르겠음(깨달음)
import heapq
def solution(stock, dates, supplies, k):
    result = 0
    daycount = 0
    hq = []   
    # stock이 k보다 작을 때까지만 반복
    while stock < k:
        # dates 배열을 돌면서 stock보다 작은 경우를 골라 hq에 넣는다. 
        for x in range(daycount,len(dates)):
            # stock보다 작은 값이 있는지 dates에서 찾는다.
            # 이 if문을 통해 stock이 다 떨어질 때까지 최대한 버틸 수 있다.
            # 만약 stock보다 dates가 작은 경우가 있다면 그날의 공급량을 최대 힙에 따라 저장한다.
            # 즉, 4일까지의 stock은 4였기에 4일에 해당하는 20이 stock에 추가되어 stock은 24가 된다.
            # 그리고 이미 추가한 날의 date는 지나치기 위해 daycount 변수를 사용하고 다시 최대한 버틴다.
            # 24인 stock보다 작은 dates의 값은 10,15가 있으므로 두 값의 supplies 값을 최대 heap에 따라 넣는다.
            # 5, 10이 supplies에 [(-10,10),(-5,5)] 의 Tuple형 List로 추가된다.
            # 24에서 10을 추가한 34가 stock이 되는 순간 while문의 조건에 따라 break가 된다.
            if dates[x] <= stock:
                # 최대 힙을 구성하는 방법(구글링)
                # 아하! 가장 큰 값을 -로 했을 때에 맨 앞으로 가지니까 Tuple형으로 저장한 heap큐의 idx = 1 값을 가져오면 가장 큰 값이 되는 것이었다.
                heapq.heappush(hq,(-supplies[x],supplies[x]))
                daycount += 1
            else:
                break
        # 최대 힙의 제일 큰 값을 가져온다
        stock += heapq.heappop(hq)[1]
        result += 1
    return result

print(solution(4,[4, 10, 15],[20, 5, 10],30))
