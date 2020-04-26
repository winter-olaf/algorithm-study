import heapq
def solution(scoville, K):
    answer = 0
    he_scoville = []
    scoville.sort()
    for i in scoville:
        heapq.heappush(he_scoville,i)
    while(he_scoville[0]<K):
        if len(he_scoville) <= 1:
            answer = -1
            break
        if len(he_scoville) >= 3:
            if he_scoville[1] <= he_scoville[2]:
                temp = he_scoville[0]+he_scoville[1]*2
            else:
                temp = he_scoville[0]+he_scoville[2]*2
        else:
            temp = he_scoville[0] + he_scoville[1] * 2
        '''
        최준원 : 이렇게 고치면 테스트케이스 3,7 빼고 통과
        if len(he_scoville) <= 1:
            answer = -1
            break
        if len(he_scoville) >= 2:
            temp = he_scoville[0] + he_scoville[1]*2
        '''
        heapq.heappop(he_scoville)
        heapq.heappop(he_scoville)
        heapq.heappush(he_scoville,temp)
        answer +=1

    return answer