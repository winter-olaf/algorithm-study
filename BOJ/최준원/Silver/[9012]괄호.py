# 60ms / 29380KB
# replace만 하면 변경된 값이 return되지만 원래 문자열은 바뀌지 않는다!!
# 프로그래머스의 쇠막대기가 떠올랐다. 쉽게 풀었음
from sys import stdin
n = int(stdin.readline())
for i in range(n):
    vps=stdin.readline().rstrip('\n')
    while True:
        if '()' in vps:
            vps = vps.replace('()','')
        else:
            break
    print('YES') if vps=='' else print('NO')