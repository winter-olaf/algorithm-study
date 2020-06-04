n,m = map(int,(input().split()))

def max_common_divisor(n,m):
    max_div = 1
    k=2
    a = min(n,m)
    while(k<=a):
        if n%k == 0 and m%k ==0:
            max_div = k
        k+=1
    return max_div

def the_least_common_multiple(n,m):
    k = max(n,m)
    while(True):
        if k%n == 0 and k%m == 0:
            return k
        k+=1

print(max_common_divisor(n,m))
print(the_least_common_multiple(n,m))