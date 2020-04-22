n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append(a+b)
for i in arr:
    print(i)