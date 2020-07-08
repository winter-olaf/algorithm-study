from sys import stdin
n = int(stdin.readline())
arr = [int(stdin.readline()) for x in range(n)]
for i in sorted(arr):
    print(i)

# 숏코딩 1위 예술적인 코드
print(*sorted(eval('int(input()),'*int(input()))))