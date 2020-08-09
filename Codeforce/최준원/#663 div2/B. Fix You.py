T = int(input())
result = []
for t in range(T):
    n,m = map(int,input().split())
    RD = []
    for i in range(n):
        RD.append(input())
    res = 0
    for i in range(n):
        if i != (n-1):
            if RD[i][m-1] == 'R':
                res+=1
        else:
            for j in range(m-1):
                if RD[i][j] == 'D':
                    res+=1
    print(res)