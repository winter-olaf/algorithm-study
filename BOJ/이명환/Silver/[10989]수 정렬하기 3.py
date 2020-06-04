import sys
n = int(sys.stdin.readline())
count = [0 for i in range(10001)]
for i in range(n):
    count[int(sys.stdin.readline())] +=1
for i,idx in enumerate(count):
    for k in range(idx):
        print(i)


