import sys
P, N = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
virus = 0

for x in range(N-1):
    virus += data[x]
    virus *= P

virus += data[-1]
print(virus%1000000007)