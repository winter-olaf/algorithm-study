'''
시간 초과
a, b, c = map(int, input().split())
if b>=c:
    print(-1)
res = 1
bb, cc = b, c
while a+b >= c:
    b+=bb
    c+=cc
    res+=1
print(res)
'''
# 21억 이하의 자연수가 주어지고, 0.35초안에 풀어야 하기 때문에 공식을 찾아야 할 듯.
# a < cx - bx
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)