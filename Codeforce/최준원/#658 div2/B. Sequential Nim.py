from sys import stdin
t=int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    if sum(a)%2 == 0:
        print("Second")
    else:
        print("First")