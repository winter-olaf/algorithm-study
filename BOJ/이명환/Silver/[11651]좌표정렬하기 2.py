import sys
n = int(sys.stdin.readline())
list = [list(map(int,(sys.stdin.readline().split()))) for i in range(n)]
a = sorted(list,key= lambda x : (x[1],x[0]))
for i,j in a:
    print(i,j)