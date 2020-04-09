# Runtime ERR
# 아마 재귀함수이기 때문에 시간이 오래 걸리는 것일 거임
# 문제풀이 30초컷
def fibo(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    return fibo(n-1)+fibo(n-2)

def solution(n):
    return fibo(n)%1234567

# 시간을 줄이기 위해 반복문을 사용함
def solution(n):
    f1,f2 = 0,1
    for i in range(2,n+1):
        # 파이썬이라 가능한 값 변환
        f1,f2 = f2, f1+f2
    return f2%1234567


print(solution(3))