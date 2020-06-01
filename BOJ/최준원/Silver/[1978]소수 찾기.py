# 보나마나 소수 알고리즘 따로 두고 해야 함
# 에라토스테네스의 체가 없이도 풀릴까? 
# 풀리네 개꿀
def sosu(n):
    r = 0
    for i in n:
        if i == 1:
            continue
        if i == 2 or i == 3:
            r+=1
            continue
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            r+=1
    return r
import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
print(sosu(arr))