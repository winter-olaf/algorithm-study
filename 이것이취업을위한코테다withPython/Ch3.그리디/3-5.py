n, k = map(int, input().split())

result = 0
# 단순한 풀이
'''
while n>=k:
    if n%k == 0:
        n//=k
        result+=1
    else:
        n -= 1
        result += 1
while n>1:
    n -= 1
    result += 1
'''
# 1을 한개씩 빼는 부분을 고려한 코드
while True:
    if n<k:
        break
    target  = (n//k)*k # 나눌 수 있는 최대 수가 몇인지 계산
    result += (n-target) # 나눌 수 있는 수가 될만큼 수를 뺀다
    n = target # 뺀만큼 더한다
    # 나누기
    result+=1
    n//=k
# 남은 수 계산
result+=(n-1)

print(result)