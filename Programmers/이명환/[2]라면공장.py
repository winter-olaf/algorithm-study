# def solution(stock, dates, supplies, k):
#     cur = 1
#     sup = 0
#     answer = 0
#     while(True):
#         if dates[sup] == cur:
#             if stock + supplies[sup] >= k-cur:
#                 #공급을 받은 재고가 남은 일수와 같거나 많을 때
#                 answer +=1
#                 break
#             elif stock < dates[sup+1] - cur:
#                 #현재 재고가 다음 받을 공급일 보다 적을 때
#                 stock += supplies[sup]
#                 answer +=1
#             elif stock >= dates[sup+1] - cur:
#                 if sum(supplies[sup:]) - supplies[sup] < k - cur:
#                     #남은 공급에서 현재 공급을 뺏을 떄 전체 남은 일 수 보다 적어질 때
#                     stock += supplies[sup]
#                     answer +=1
#             sup += 1
#         cur +=1
#         stock -= 1
#     return answer

#테스트 1, 11 통과.. 어느 부분에서 틀린지 잘 모르겠음...


#
# stock	dates	supplies	k	result
# 4	[4,10,15]	[20,5,10]	30	2


def solution(stock, dates, supplies, k):
    import heapq

    answer = 0
    # 범위 시작점입니다.
    idx = 0
    # 1. 최대 힙 기반 우선순위 큐를 생성합니다.
    pq = []

    # 2. stock < k일 때까지 다음을 반복합니다.
    while stock < k:
        # 1. idx ~ dates의 끝까지 반복합니다.
        for i in range(idx, len(dates)):
            # 1. stock 이 dates[i]보다 작으면 반복을 멈춥니다.
            if stock < dates[i]:
                break
            # 2. 우선순위 큐에 supplies[i]를 넣습니다.
            heapq.heappush(pq, -supplies[i])
            # 3. 시작점을 i+1지점으로 옮깁니다.
            idx = i + 1

        # 2. 우선순위 큐에서 데이터를 꺼내 stock에 더해줍니다.
        stock += (heapq.heappop(pq) * -1)
        # 3. 공급 횟수 answer에 1을 더해줍니다.
        answer += 1

    return answer