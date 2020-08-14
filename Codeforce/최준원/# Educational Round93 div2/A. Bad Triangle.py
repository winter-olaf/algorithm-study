from sys import stdin
def triangle():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    for i in range(n-2):
        for j in range(i+2,n-1):
            print(arr[i])
            if arr[i] + arr[i+1] < arr[i+j]:
                return "%d %d %d" % (i+1, i+2, i+3)
    return -1

t = int(input())
for x in range(t):
    print(triangle())