import sys

n = int(sys.stdin.readline())
localG = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start,end = 0,max(localG)

while start<=end:
    mid = (start+end)//2
    amount = 0

    for i in localG:
        if i <= mid:
            amount += i
        else:
            amount += mid

    if amount>m:
        end = mid-1
    else:
        start = mid+1

print(end)