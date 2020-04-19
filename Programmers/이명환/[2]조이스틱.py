def solution(name):
    # 알파벳을 맞추는 최소 횟수를 저장하는 배열 m을 만듬 (+1은 조이스틱이'A'부터 시작이기 떄문에)
    m = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    answer = 0
    idx = 0
    
    while True:
        answer += m[idx]
        m[idx] = 0
        if sum(m) == 0:
            break
        left,right =(1,1)
        #m[idx-left] or m[idx-right]가 0이 아닌 횟수가 나올 떄 까지
        while m[idx-left] <=0:
            left +=1
        while m[idx+right] <=0:
            right +=1
        answer += left if left <right else right
        idx += -left if left <right else right


    return answer