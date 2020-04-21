a,b = map(int,input().split())
def solution(a,b):
    # return {a<b:'<', a>b:'>'}.get(True,'==')
    return {a<b:'<', a==b:'=='}.get(True,'>')
print(solution(a,b))