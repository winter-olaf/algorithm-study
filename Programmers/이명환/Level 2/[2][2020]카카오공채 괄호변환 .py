#1,3,4
def solution(w):
    if w == '':
        return ''
    u,v = divide(w)
    if check(u,v) == True:
        return u + solution(v)
    else:
        return process(u,v)

# 2번 문자열 u,v로 나누기
def divide(w):
    u= ''
    v =''
    cnt = 0
    idx = 0
    for i in w:
        if i == '(':
            idx +=1
            cnt +=1
        else:
            idx += 1
            cnt -=1
        if cnt ==0:
            break
    u += w[:idx]
    v += w[idx:]
    return u,v

#3번 "올바른 괄호문자 판단"
def check(u,v):
    temp = 0
    open = True
    for i in u:
        if i == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            return False
    return True

#4번 과정
def process (u,v):
    k = ''
    k += '('
    k += solution(v)
    k += ')'
    for i in u[1:-1]:
        if i == '(':
            k += ')'
        else:
            k += '('
    return k