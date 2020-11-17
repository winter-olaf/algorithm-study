import sys

arr = []
n = int(sys.stdin.readline())

for i in range(n):
    meat1,meat2 = map(int,sys.stdin.readline().split())
    arr.append((meat1,meat2))

arr = sorted(arr)
fast_start = arr[0][0]
fast_end = arr[0][1]
cnt = 1

if len(arr) >1:
    for start,end in arr[1:]:
        if start >= fast_end:
           cnt+=1
           fast_start = start
           fast_end = end
        elif end <= fast_end:
            fast_start = start
            fast_end = end
print(cnt)
