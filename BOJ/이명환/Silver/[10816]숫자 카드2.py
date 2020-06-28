import sys

n = int(sys.stdin.readline())
posess = sys.stdin.readline().split()
m = int(sys.stdin.readline())
criminate = sys.stdin.readline().split()
dic = {}

for i in posess:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
for k in criminate:
    if k in dic:
        if k == criminate[-1]:
            print(dic[k])
        else:
            print(dic[k],end=' ')
    else:
        print('0',end=' ')