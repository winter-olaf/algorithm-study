import sys
import itertools

n = sys.stdin.readline().split()
sequence = list(map(int,sys.stdin.readline().split()))
N = int(n[0])
S = int(n[1])
result = 0
for i in range(1,N+1):
    for k in list(itertools.combinations(sequence,i)):
        if sum(k) == S:
            result +=1
print(result)