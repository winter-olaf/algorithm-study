import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = sys.stdin.readline()
    result = 0
    Oth = 0
    for j in a:
        if j == 'O':
            Oth += 1
            result += (Oth*1)
        else:
            Oth = 0
    arr.append(result)
for i in arr:
    print(i)


