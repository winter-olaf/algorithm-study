def convert(number, base):
    t = '0123456789ABCDEF'
    q, r = divmod(number, base)
    if q == 0:
        return t[r]
    else:
        return convert(q, base) + t[r]
        
def solution(n):
    a = convert(n,3)[::-1]
    res, cnt = 0, len(a)-1
    for i in a:
        res += int(i)*(3**cnt)
        cnt-=1
    return res

solution(125)