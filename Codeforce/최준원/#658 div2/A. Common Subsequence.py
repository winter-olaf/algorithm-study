from sys import stdin
t = int(input())
result =  []
for i in range(t):
    y_or_n = True
    n,m = map(int,stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    for i in a:
        if i in b:
            print("YES")
            print('1 '+str(i))
            y_or_n = False
            break
    if y_or_n == True:
        print("NO")
for i in result:
    print(i)