import sys

n,k = map(int,sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

index = len(arr) -1
cnt = 0

while(k!=0):
    if(arr[index]<=k):
        temp = int(k/arr[index])
        k -= arr[index]*temp
        cnt += temp
    else:
        index-=1
print(cnt)