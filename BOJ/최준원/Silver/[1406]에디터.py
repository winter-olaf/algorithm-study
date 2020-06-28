import time
from sys import stdin

'''
# 시간 초과. 아마 del이 문제가 아닌가?
start = time.time()
a = list(input())
m = int(input())
commands = [input() for x in range(m)]
# 커서 변수
idx = len(a)
for command in commands:
    if command[:1] == "P":
        a.insert(idx,command[2:])
        idx+=1
    elif command == "L":
        if idx == 0:
            continue
        else:
            idx -= 1
    elif command == "D":
        if idx == len(a):
            continue
        else:
            idx += 1
    elif command == "B":
        if idx == 0:
            continue
        else:
            del a[idx-1]
            idx-=1
print("".join(a))
print(time.time()-start)
'''

'''
# stdin도 마찬가지로 에러.
start = time.time()
a = list(stdin.readline().strip())
m = int(input())
commands = [stdin.readline().strip() for x in range(m)]
# 커서 변수
idx = len(a)
for command in commands:
    if command[:1] == "P":
        a.insert(idx, command[2:])
        idx += 1
    elif command == "L":
        if idx == 0:
            continue
        else:
            idx -= 1
    elif command == "D":
        if idx == len(a):
            continue
        else:
            idx += 1
    elif command == "B":
        if idx == 0:
            continue
        else:
            del a[idx-1]
            idx -= 1
print("".join(a))
print(time.time()-start)
'''
# 데큐를 사용하자...