t = int(input())
num = [list(map(int,input().split())) for x in range(t)]
for i in range(t):
    print("Case #%d: %d" %(i+1, num[i][0]+num[i][1]))