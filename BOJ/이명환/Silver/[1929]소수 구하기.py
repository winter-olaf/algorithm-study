import sys

mnList = list(map(int,sys.stdin.readline().split()))
M = mnList[0]
N = mnList[1]
x = M
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

while(x <=N):
    if is_prime(x):
        print(x)
    x+=1
