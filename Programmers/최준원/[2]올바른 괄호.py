# 지금까지 풀어 본 문제 중 제일 쉬웠다고 생각했는데 테스트 케이스 5, 11 통과 못함.
# 92.3/100
def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    elif s.count('(') == s.count(')'):
        return True
    else:
        return False


# 아! ())(() 같은 경우는 False가 떠야되네!
# 엥 근데 이번엔 5, 11, 17 틀림
def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    opencnt = 0
    closecnt = 0
    for x in s:
        if x == '(':
            opencnt+=1
        elif x == ')':
            closecnt+=1
        if opencnt < closecnt:
            return False
        elif opencnt == closecnt:
            return True

# 이번엔 될거라 생각했지만 17을 통과 못함 ㅡㅡ
def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    opencnt = 0
    closecnt = 0
    for x in s:
        if x == '(':
            opencnt+=1
        elif x == ')':
            closecnt+=1
        if opencnt < closecnt:
            return False
    if s.count('(') == s.count(')'):
        return True

# 이렇게 하면 다시 5, 11통과 안됨
def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    opencnt = 0
    closecnt = 0
    if s.count('(') != s.count(')'):
        return False
    else:
        for x in s:
            if x == '(':
                opencnt+=1
            elif x == ')':
                closecnt+=1
            if opencnt < closecnt:
                return False
            elif opencnt == closecnt:
                return True

# 그냥 스택 사용
# 뭐가 다른지 나중에 확인할 생각
# 100/100
def solution(s):
    q = 0
    for _ in s:
        if _ == '(':
            q += 1
        else:
            if not q:
                return False
            q -= 1
    if q == 0:
        return True
    else:
        return False
            

    
    
    