# 시간을 따로 재야 하니까 딕셔너리를 사용할까? 아니 너무 번거로워지는 것 같기도 하고

def solution(bridge_length, weight, tlist):
    result = 0
    tqueue = [0] * bridge_length # 대기열 생성
    tlist = tlist[::-1] # pop의 최적화를 위해 대기하는 트럭의 리스트를 뒤집어 준다

    while tqueue:
        result += 1 # 1초가 지났음
        print(tqueue) # 대기열 확인용
        tqueue.pop(0) # 1초마다 대기열을 당겨줌
    
        if tlist: # 건너야 할 트럭이 남아 있는 동안 반복
            if sum(tqueue) + tlist[-1] <= weight:
                tqueue.insert(1,tlist.pop())
            else:
                tqueue.append(0)
    return result

print(solution(	2, 10, [7, 4, 5, 6]))
        
        
        
        
        
        
