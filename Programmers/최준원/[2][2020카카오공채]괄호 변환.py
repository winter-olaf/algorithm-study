# 문자열 분리 함수
def uv(w):
    u = ''
    v = ''
    stack = 0
    for idx,val in enumerate(w):
        # 균형잡힌 괄호 문자열 u,v로 반환하기 위해 
        # stack이 0인 경우 = '('와')'의 수가 동일하면 break
        if val == '(':
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            break
    u += w[:idx+1]
    v += w[idx+1:]
    return u,v

# 올바른 괄호 문자열 체크 함수
def True_or_False(p):
    stack = 0
    for i in p:
        if i == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return True

def solution(p):
    ans = ''
    # 1,2
    if p == '':
        return ''
    else:
        u,v = uv(p)
    # 3
    if True_or_False(u) == True:
        # 3-1
        ans += u
        # 문자열 v에 대한 재귀함수
        ans += solution(v)
    # 4
    else:
        # 4-1
        ans += '('
        # 4-2
        ans += solution(v)
        # 4-3
        ans += ')'
        # 4-4,4-5
        for i in u[1:-1]:
            if i == '(':
                ans += ')'
            else:
                ans += '('
    return ans

print(solution("()))((()"))