import sys

n = sys.stdin.readline().split()
N = int(n[0])
K = idx = int(n[1]) -1
yosef = []
table = [i for i in range(1,N+1)]
while(table):
    while(idx>len(table)-1):
        idx -= len(table)
    yosef.append(table.pop(idx))
    idx += K
yosef = ', '.join([str(_) for _ in yosef])
print('<',yosef,'>',sep='')