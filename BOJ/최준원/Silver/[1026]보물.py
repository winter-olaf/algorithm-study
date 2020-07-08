# 60ms / 29380KB
from sys import stdin
def treasure(n,a,b):
    result = 0
    for i in range(n):
        result+=a[i]*b[i]
    return result
n = int(input())
a = sorted(list(map(int, stdin.readline().split())))
b = sorted(list(map(int, stdin.readline().split())),reverse=True)
print(treasure(n,a,b))