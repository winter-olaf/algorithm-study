# 실행 시간이 오래걸림
def solution(arr):
    stack = 0
    ans = 0
    # 레이저를 확인하기 위한 bool var
    laser = False

    for i in arr:
        if i == '(':
            laser = True
            stack += 1
        else:
            # 레이저가 True이면 지금까지 모인 stack의 값에서 1을 뺀 만큼 결과에 더한다.
            if laser == True:
                ans += stack - 1
                laser = False
            # 레이저가 False이면 쇠막대기가 끝나는 것을 의미하므로 답만 하나 추가한다.
            else:
                ans += 1
            # 두 경우 모두 공통적으로 스택을 하나 제거해야 함
            # 레이저일 경우 레이저를 만들기 위해서 ()가 필요했었기 때문에 하나 제거하고,
            # 레이저가 아닐 경우 쇠막대기가 끝나기 때문에 하나 제거하는 것.
            stack -= 1
    return ans
            



# 더 효율적으로 풀어 봄
def solution(arr):
    stack = 0
    ans = 0
    # 레이저를 따로 표시해 둠
    arr = arr.replace('()','z')
    for i in arr:
        if i == '(':
            stack += 1
        elif i == 'z':
            ans += stack
        else:
            stack -= 1
            ans += 1

    return ans


print(solution('()(((()())(())()))(())'))
            
            

    