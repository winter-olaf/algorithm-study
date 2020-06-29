import sys

num = int(sys.stdin.readline())
real_measure = sorted(list(map(int,sys.stdin.readline().split())))
N = real_measure[0]*real_measure[-1]
print(N)