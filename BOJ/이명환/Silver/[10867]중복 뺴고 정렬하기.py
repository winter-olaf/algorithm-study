import sys
n = int(sys.stdin.readline())
list = list(map(int,(sys.stdin.readline().split())))
a = sorted(set(list))
a = " ".join([str(_) for _ in a])
print(a)