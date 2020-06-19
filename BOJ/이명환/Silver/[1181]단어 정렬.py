import sys
from itertools import combinations
n = int(sys.stdin.readline())
dic = []
temp_len = 0
max_len = 0
a= 1
for i in range (n):
    temp = sys.stdin.readline().rstrip('\n')
    dic.append(temp)
    temp_len = len(temp)
    if max_len < temp_len:
        max_len = temp_len
dic = sorted(set(dic))
while(a <= max_len ):
    for k in dic:
        if len(k) == a:
            print(k)
    a+=1