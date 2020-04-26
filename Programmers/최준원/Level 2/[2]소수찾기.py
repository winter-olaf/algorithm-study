#### 내 풀이

import itertools
import math

# 처리속도를 빠르게 하기 위해 소수 판별 함수를 따로 둠
def isPrime(n):
    if n == 1 or n == 0:
            return False
    elif n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def solution(num):
    result = 0
    # 순열 저장용 리스트
    arr = []
    # 문자열 input을 하나씩 떼내어 list로 변환
    num = [i for i in num]
    
    # 순열을 배열에 저장
    for i in range(1,len(num)+1):
        # arr+=list(map(''.join, itertools.permutations(num,i))) 였는데 이렇게하면 01과 1의 구분이 되지 않으므로 int형으로 변환
        arr+=list(map(int,list(map(''.join, itertools.permutations(num,i)))))

    # 중복값 제거
    arr = set(arr)
    
    for i in arr:
        if isPrime(i) == True:
            result += 1
    return result


#### 1등 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
