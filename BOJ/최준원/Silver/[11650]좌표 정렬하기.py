import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a,b))
for a,b in sorted(arr):
    print(a,b)