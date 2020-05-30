# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
n = int(input())
sort_list = [int(sys.stdin.readline()) for i in range(n)]
for i in sorted(sort_list):
    print(i)