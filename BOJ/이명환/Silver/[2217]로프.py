import sys

arr = []
n = int(sys.stdin.readline())

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

max = arr[-1]
for index,node in enumerate(arr):
    if (n-index)*node >= max:
        max = (n-index)*node
print(max)