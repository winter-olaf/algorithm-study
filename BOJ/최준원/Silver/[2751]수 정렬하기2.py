import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr):
    print(i)

# 2
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(n)]
for i in sorted(arr):
    print(i)