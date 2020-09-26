from sys import stdin
t = int(stdin.readline())
num = [list(map(int,stdin.readline().split())) for x in range(t)]
for i in range(t):
    print(num[i][0]+num[i][1])