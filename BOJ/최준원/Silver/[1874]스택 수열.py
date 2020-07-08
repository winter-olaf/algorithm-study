# 이게 뭔소리여?
# 아 써보니까 알겠다. 그냥 스택 하나를 임시로 두고 거기다가 넣으면서 결과값을 계속 뽑아오면 됨. 다시 말해 pop은 총 n번 하게 될 것임.
from sys import stdin,stdout
n = int(input())
goal = []
for _ in range(n):
    goal.append(int(stdin.readline())) # 목표
def stacksuyeol():
    stack = [] # 임시 스택
    result = []
    cnt = 1
    for g in goal:
        while cnt <= g: # 원하는 값이 나올 때까지 카운트 올리면서 푸쉬(임시 스택에 저장)
            # 1. 예제 1의 경우 [1,2,3,4]까지 쌓이고 나면 
            stack.append(cnt)
            result.append('+')
            cnt+=1
        # 만약 stack의 pop 값과 g(주어진 목표의 값)이 같다면? 그대로 pop
        if g == stack[-1]: # 2. if문의 조건이 성립되므로 pop 실행
            stack.pop()
            result.append('-')
        # 다른 풀이를 보니까 이렇게 조건을 설정하면 pop이 자동으로 됨.
        # if g == stack.pop():
        #     result.append('-')
        else: # 만약 pop하는 값과 다르면 해당 수열은 만들 수가 없음.
            return 'NO'
    return '\n'.join(result)
print(stacksuyeol())