import sys
arr = list(map(int,sys.stdin.readline().split()))
res = 0
for i in arr:
    res += i**2
print(res%10)