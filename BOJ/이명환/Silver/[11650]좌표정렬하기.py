# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
n = int(input())
list = [list(map(int,(sys.stdin.readline().split()))) for i in range(n)]
a = sorted(list)
for i,j in a:
    print(i,j)