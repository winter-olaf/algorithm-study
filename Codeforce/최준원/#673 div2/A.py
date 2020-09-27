t = int(input())
for test in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in arr:
        for j in range(len(arr)-1):
            