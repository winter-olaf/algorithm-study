import sys
from itertools import combinations
    
program__end = 1
while(program__end == 1):
    line = list(map(int,sys.stdin.readline().split()))
    k = line[0]
    arr = line[1:]
    arr_com = list(combinations(arr, 6))
    for i in arr_com:
        print(str(i).lstrip('(').rstrip(')').replace(',',''))
    print('\n',end='')
    if k == 0:
        program__end = 0
# 시간초 걸릴줄 알았는데 맞네;..