# 라이브러리를 쓰면 진짜 간단한 문제이긴 한데 클래스 하나 만들자
# 시간초과!
# import sys
# a,b = map(int,sys.stdin.readline().split())
# def gg(n):
#     e = 0
#     s = 0
#     while n>1:
#         if n%2==0:
#             n//=2
#             e+=1
#         if n%3==0:
#             n//=3
#             s+=1
#     return e,s
# def solve(a,b):
#     e=[]
#     s=[]
#     e.append(gg(a)[0])
#     e.append(gg(b)[0])
#     s.append(gg(a)[1])
#     s.append(gg(b)[1])
#     return (2**min(e))*(3**min(s)),(2**max(e))*(3**max(s))
# for i in solve(a,b):
#     print(i)

# min, max 말고 sort를 쓰자
# 또 시간 초과!
# import sys
# a,b = map(int,sys.stdin.readline().split())
# def gg(n):
#     e = 0
#     s = 0
#     while n>1:
#         if n%2==0:
#             n//=2
#             e+=1
#         if n%3==0:
#             n//=3
#             s+=1
#     return e,s
# def solve(a,b):
#     e=[]
#     s=[]
#     e.append(gg(a)[0])
#     e.append(gg(b)[0])
#     s.append(gg(a)[1])
#     s.append(gg(b)[1])
#     return sorted(e),sorted(s)
# print(2**solve(a,b)[0][0]*3**solve(a,b)[1][0])
# print(2**solve(a,b)[0][-1]*(3**solve(a,b)[1][-1]))

# 제곱이 아니라 for문으로 해볼까
# append를 쓰면 안된다!
# import sys
# a,b = map(int,sys.stdin.readline().split())
# def gg(n):
#     e = 0
#     s = 0
#     while n>1:
#         if n%2==0:
#             n//=2
#             e+=1
#         if n%3==0:
#             n//=3
#             s+=1
#     return e,s
# def solve(a,b):
#     e=[]
#     s=[]
#     e.append(gg(a)[0])
#     e.append(gg(b)[0])
#     s.append(gg(a)[1])
#     s.append(gg(b)[1])
#     return sorted(e),sorted(s)
# minr=1
# maxr=1
# for i in range(solve(a,b)[0][0]):
#     minr*=2
# for i in range(solve(a,b)[1][0]):
#     minr*=3
# for i in range(solve(a,b)[0][1]):
#     maxr*=2
# for i in range(solve(a,b)[1][1]):
#     maxr*=3
# print(minr,maxr,sep="\n")

# 걍 gcd lcm 쓰자.
# 최소공배수 X 최대공약수 : 두 수의 곱
import sys
from math import gcd
a,b=map(int,sys.stdin.readline().split())
def lcm(a,b):
    return a*b//gcd(a,b)
print(gcd(a,b))
print(lcm(a,b))
