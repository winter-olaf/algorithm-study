import math
def solution(w,h):
    # 대각선이기 때문에 비율은 고정될 수 있다는 것을 생각하자
    # 최대공약수 나눈 뒤, 못 쓰게 되는 사각형이 반복되는 수 (최대공약수로 나눈 비율)을 구하면 끝
    cal = math.gcd(w,h)
    # 최대공약수로 나눈 비율을 더한 뒤, 1을 빼준다. 머릿속으로 대각선을 그려 보면,
    # 겹치는 부분이 하나 있기 때문이다.
    answer = (w*h) - (w//cal + h//cal - 1) * cal
    return answer