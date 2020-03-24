# 30/100
def solution(prog,speed):
    ans = [] 

    while prog:
        cnt = 0 # 배포용 변수. pop을 사용하기 때문에 초기화 해야 함
        
        # 과정이 하나일 경우
        if len(prog) == 1:
            ans.append(1)    
            break
        
        # 차례차례 진도 나가기
        for i in range(len(prog)): 
            prog[i] += speed[i]
        
        # while문의 중첩으로 한번에 배포할 수 있는 작업의 수를 계산해 준다
        while prog: 
            if prog[0] >= 100:
                prog.pop(0)
                cnt+=1
            else:
                break
        
        # 배포용 변수가 있을 경우 결과 리스트에 추가한다.
        if cnt != 0: 
            ans.append(cnt)

    return ans

# 10/100 개선했다고 생각했는데 오히려 더 망함
def solution(prog,speed):
    ans = [] # 

    while prog:
        cnt = 0 # 배포용 변수. pop을 사용하기 때문에 초기화 해야 함
        
        # 과정이 하나일 경우
        if len(prog) == 1:
            ans.append(1)    
            break

        # while문의 중첩으로 한번에 배포할 수 있는 작업의 수를 계산해 준다
        while prog: 
            if prog[0] >= 100:
                prog.pop(0)
                cnt+=1
            else:
                break   

        # 차례차례 진도 나가기
        for i in range(len(prog)): 
            prog[i] += speed[i]
            
            # 첫번째 작업이 100 이상이 되는 순간 바로 loop를 빠져나와야 하는데 그걸 빼먹었다
            if prog[0] >= 100:
                break
        
        # 배포용 변수가 있을 경우 결과 리스트에 추가한다.
        if cnt != 0: 
            ans.append(cnt)

    return ans

# 100/100
# for 문을 사용하면 더하기를 한 차례 완료할 때까지 기다려야 하리 때문에 오류가 자꾸 뜬다. 따라서 add를 이용해 한번의 loop에 모든 prog의 원소가 계산되도록 했다
from operator import add
def solution(prog,speed):
    ans = [] 

    while prog:
        cnt = 0 # 배포용 변수. pop을 사용하기 때문에 초기화 해야 함
        
        # 과정이 하나일 경우
        if len(prog) == 1:
            ans.append(1)    
            break
        
        # for문으로 순차적으로 작업 진도를 나가면 앞의 작업이 100이 되었더라도 뒤의 작업을 진행하게 된다. 
        # 따라서 add를 사용해 
        prog = list(map(add,prog,speed))

        # while문의 중첩으로 한번에 배포할 수 있는 작업의 수를 계산해 준다
        while prog: 
            if prog[0] >= 100:
                prog.pop(0)
                # 당연히 speed도 바꿔 줘야 하는데 이부분을 생각 안했다 멍청하게 아아아아!
                speed.pop(0)
                cnt+=1
            else:
                break
                
        # 배포용 변수가 있을 경우 결과 리스트에 추가한다.
        if cnt != 0: 
            ans.append(cnt)

    return ans
print(solution([93,30,55],[1,30,5]))

# 파이서닉 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]