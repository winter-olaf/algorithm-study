# 15/100
n = int(input())


def solution(n):
    result = 0
    for x in range(1, n+1):
        while x <= n:
            if x == n:
                result += 1
                break
            x += x+1
    return result

# 15/100
def solution(n):
    result = 0
    xl = []
    
    for x in range(1,n+1):
        count = x  # 기준값을 유지하며 비교하기 위한 변수를 별도로 생성
        while True:
            if count == n:
                result+=1
                xl.append(x)
                break
            elif count >= n:
                break
            else:
                count += count+1
    return result,xl

print(solution(n))

# 100/100 2중 for문

def solution(n):
    result = 1  # 자기 자신을 계산한 뒤 시작
    for x in range(1, n//2+2):
        count = 0
        for y in range(x, n//2+2):
            count += y
            if count == n:
                result += 1
                break
            elif count > n:
                break
    return result

# 100/100 for + while


def solution(n):
    result = 1  # 자기 자신을 계산한 뒤 시작
    for x in range(1, n//2+2):
        s = 0  # 합 계산
        while s < n:
            if s == 0:
                s = x
                tmp = x  # 더하기를 위한 임시 값
            else:
                tmp += 1
                s += tmp
                if s == n:
                    result += 1
    return result
            
# 등차수열을 사용한(?) 다른 사람의 파이서닉한 풀이
def expressions(num):
    return len([i for i in range(1, num+1, 2) if num % i is 0])
