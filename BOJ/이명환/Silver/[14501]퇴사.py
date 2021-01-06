import sys
n = int(sys.stdin.readline())
t_p = []
for i in range(n):
    t,p = map(int,sys.stdin.readline().split())
    t_p.append((t,p))

print(t_p)