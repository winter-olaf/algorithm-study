# Very EZEZ
def solution(s):
    ans = ''
    tmp = list(map(int,s.split(' ')))
    a = str(min(tmp))
    b = str(max(tmp))
    ans = (a,b)
    return ' '.join(ans)
    

print(solution('-1 -2 -3 -4'))

# 기는 내 위에 나는 사람 있더라
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))