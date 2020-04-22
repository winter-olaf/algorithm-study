arr = []
while True:
    a, b = map(int, input().split())
    arr.append(a+b)
    if a == 0 and b == 0:
        for i in arr[:-1]:
            print(i)
        break
