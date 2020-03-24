# 시간을 따로 재야 하니까 딕셔너리를 사용할까? 아니 너무 번거로워지는 것 같기도 하고

def solution(bridge_length, weight, tlist):
    result = 0
    tqueue = [0] * bridge_length # 대기열 생성
    tlist = tlist[::-1] # pop의 최적화를 위해 대기하는 트럭의 리스트를 뒤집어 준다

    while tqueue:
        result += 1 # 1초가 지났음
        tqueue.pop(0) # 1초마다 대기열을 당겨줌
    
        if tlist: # 건너야 할 트럭이 남아 있는 동안 반복
            if sum(tqueue) + tlist[-1] <= weight:
                tqueue.append(tlist.pop())
            else:
                tqueue.append(0)
    return result

# pop으로 뒤집지 않았는데 30ms 빨랐다
def solution(bridge_length, weight, tlist):
    result = 0
    tqueue = [0] * bridge_length  # 대기열 생성

    while tqueue:
        result += 1  # 1초가 지났음
        tqueue.pop(0)  # 1초마다 대기열을 당겨줌
        if tlist:  # 건너야 할 트럭이 남아 있는 동안 반복
            if sum(tqueue) + tlist[0] <= weight:
                tqueue.append(tlist.pop(0))
            else:
                tqueue.append(0)
    return result

print(solution(100	,100,	[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))