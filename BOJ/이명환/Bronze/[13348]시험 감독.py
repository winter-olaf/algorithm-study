import sys
import math

n = int(sys.stdin.readline())
candidate = list(map(int,sys.stdin.readline().split()))
b,c = map(int,sys.stdin.readline().split())
cnt = 0
for i in range(n):
    cnt+=1
    student = candidate[i]
    student-=b
    sub_supervisor = c

    if student <=0:
        continue
    remain = student/sub_supervisor
    if remain < 1:
        cnt+=1
        continue
    else:
        cnt+=math.ceil(remain)


print(cnt)