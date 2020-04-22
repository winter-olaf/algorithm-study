arr = []
while True:
    try:
        a, b = map(int, input().split())
        arr.append(a+b)
    except:
        for i in arr:
            print(i)
        break
