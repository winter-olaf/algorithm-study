import sys
N = int(sys.stdin.readline())

clap = 0
for i in range(1, N+1):
    tmp = str(i)

    if '3' in tmp:
        clap += tmp.count('3')
    if '6' in tmp:
        clap += tmp.count('6')
    if '9' in tmp:
        clap += tmp.count('9')

print(clap)
