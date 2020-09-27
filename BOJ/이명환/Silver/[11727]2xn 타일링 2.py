import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    sys.exit()

a = [0 for _ in range(n+1)]
a[0], a[1] = 1, 1
for i in range(2, n+1):
    a[i] = (a[i-1] + 2 * a[i-2]) % 10007

print(a[n])