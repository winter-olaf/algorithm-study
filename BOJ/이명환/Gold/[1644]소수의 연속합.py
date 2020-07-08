import sys

n = int(sys.stdin.readline())
def is_prime(x):
    if x <2:
        return False
    if x in (2,3):
        return True
    if x%2 == 0 or x%3 == 0:
        return False
    if x < 9:
        return True
    k,l=5, x**0.5
    while k<=l:
        if x%k == 0 or x %(k+2) == 0:
            return False
        k+=6
    return True

prime = []
for i in range(2,n+1):
    if is_prime(i):
        prime.append(i)
answer = 0
m = 0
while(True):
    if n == 1:
        break
    if prime[m] >= n/2:
        if n in prime:
            answer+=1
        break
    result = 0
    k = m
    while(True):
        result += prime[k]
        if result == n:
            answer +=1
            break
        elif result > n:
            break
        k+=1
    m+=1


print(answer)
#pypy3로 풀음