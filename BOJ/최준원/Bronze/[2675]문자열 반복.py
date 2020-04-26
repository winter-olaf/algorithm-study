import sys
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    r,s = map(str,sys.stdin.readline().split())
    r = int(r)
    repeatedString = ''
    for j in s:
        repeatedString += j*r
    arr.append(repeatedString)
for i in arr:
    print(i)
