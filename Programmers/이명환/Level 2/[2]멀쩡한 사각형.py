#직선의 끝점의 좌표위치의 최대공약수가 1일 떄
#겹치는 사각형의 개수 = w+h -1
#else 최대 공약수 가 g일 때, 겹치는 사각형의 개수 =  g*((w/g)+(h/g)-1) = w+h - 최대공약수
import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

# def computeGCD(x, y):
#     if x > y:
#         small = y
#     else:
#         small = x
#     for i in range(1, small + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             gcd = i
#
#     return gcd