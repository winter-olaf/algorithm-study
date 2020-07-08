from sys import stdin
n=int(input())
a=map(int,stdin.readline().split())
for i in sorted(set(a)):
    print(i,end=' ')