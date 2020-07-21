import sys

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

while (True):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    a = 2
    while(True):
        if is_prime(a):
            pass
        else:
            a+=1
            continue
        b = n -a
        if is_prime(b):
            print(n,'=',a,'+',b)
            break
        else:
            a+=1