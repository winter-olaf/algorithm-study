from sys import stdin
def lotto(n,m):
    result = []
    while True:
        for _ in range(n):
            i = 1
            while i<=n:
                print(1)

t = int(input())
for _ in range(t):
    n,m = map(int,stdin.readline().split())
    print(lotto(n,m))