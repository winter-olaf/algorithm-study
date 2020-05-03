# # 61.9/100 
# # 테스트케이스 3,7,15 실패, 효율성 테스트 죄다 실패
# import heapq
# def solution(scoville, K):
#     ans = 0
#     hq = []
#     for i in scoville:
#         heapq.heappush(hq,i)
#     # In this def, heapq needs at least 2 elements
#     while len(hq)>=2:
#         if hq[0] < K:
#             heapq.heappush(hq,hq[0] + (hq[1]*2))
#             heapq.heappop(hq)
#             heapq.heappop(hq)
#             ans += 1
#         # If minimum number is bigger or same than K
#         if min(hq) >= K:
#             return ans
#     # If heapq has only one element smaller than K
#     return -1


# 테스트케이스 3,7 실패
import heapq
def solution(scoville, K):
    ans = 0
    # for문이 아니라 heapify를 사용해 힙 큐로 변경
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        if scoville[0] < K:
            heapq.heappush(scoville, scoville[0] + (scoville[1]*2))
            heapq.heappop(scoville)
            heapq.heappop(scoville)
            ans += 1
        if min(scoville) >= K:
            return ans
    return -1

# 76.2/100
# 테스트 케이스 모두 통과, 효율성 테스트 모두 탈락
import heapq
def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        if scoville[0] < K:
            # heappop을 두번 하는 부분이 오류라고 판단되어 제거하고 heappush 전 과정에 해결하도록 넣음
            heapq.heappush(scoville, heapq.heappop(
                scoville) + (heapq.heappop(scoville)*2))
            ans += 1
        if min(scoville) >= K:
            return ans
    return -1

# 최종 통과
import heapq
def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    # while문이 끝났을 때 결과를 리턴하고, 예외의 경우를 while 문 안쪽으로 넣었다.
    while scoville[0]<K:
        if len(scoville) == 1:
            if scoville[0] >= K:
                return ans
            else:
                return -1
        heapq.heappush(scoville, heapq.heappop(
            scoville) + (heapq.heappop(scoville)*2))
        ans += 1
    return ans


print(solution([1,2,3],11))
