# Very EZEZ
def solution(s):
    ans = ''
    tmp = list(map(int,s.split(' ')))
    a = str(min(tmp))
    b = str(max(tmp))
    ans = (a,b)
    return ' '.join(ans)
    

print(solution('-1 -2 -3 -4'))