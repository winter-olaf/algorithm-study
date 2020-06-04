import sys
dic = []
for i in range(int(sys.stdin.readline().rstrip('\n'))):
    li = sys.stdin.readline().split()
    x = int(li[0])
    dic.append([x,li[1]])
for x,y in sorted(dic, key=lambda x:x[0]):
    print(x,y)