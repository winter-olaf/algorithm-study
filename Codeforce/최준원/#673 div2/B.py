from sys import stdin
tc = int(input())
for test in range(tc):
    n,t = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    res = [0]*n
    count = n
    for i1,v1 in enumerate(arr):
        if count <= 1:
            break
        for i2,v2 in enumerate(arr[i1+1:]):
            if count <= 1:
                break
            if v1+v2 == t:
                print('인덱스' , i1)
                print('b인덱스', i2)
                res[i1] = 1
                count-=2
    print(res)
