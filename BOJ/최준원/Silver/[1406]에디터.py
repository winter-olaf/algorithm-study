import time
from sys import stdin, stdout

'''
# 시간 초과. 아마 del이 문제가 아닌가? 아니, 슬라이싱 자체가 시간을 잡아먹는듯
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
# 파이썬 시간제한 문제 너무하네 정말
# 아 스택을 두개 쓴다는게 이거구만
# 런타임 에러? why?
'''
# "\n" 지우는 방법 : strip 혹은 [:-1]
l_stack = list(stdin.readline()[:-1])
r_stack = []
m = int(input())
commands = [stdin.readline().strip() for x in range(m)]
for command in commands:
    if command[0] == 'P':
        l_stack.append(command[2])
        # l_stack이 남아있어야만 pop을 실행(이후 D,B 모두 동일)
    elif command[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif command[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif command[0] == 'B' and l_stack:
        l_stack.pop()
print("".join(l_stack+r_stack[::-1]))
'''
# 대체 왜 런타임 에러가 뜨지??
'''
l_stack = list(stdin.readline()[:-1])
m = int(stdin.readline())
r_stack = list()
for i in range(m):
    command = stdin.readline()
    if command[0] == 'P':
        l_stack.append(command[2])
    elif command[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif command[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif command[0] == 'B' and l_stack:
        l_stack.pop()
stdout.write(''.join(l_stack+r_stack[::-1]))
'''
# 이건 되는거야? 뭔차이지?
'''
import sys 
left_stack = list(sys.stdin.readline()[:-1]) 
right_stack = list() 
testcase = int(sys.stdin.readline()) 
for _ in range(testcase): 
    cmd = sys.stdin.readline() 
    if cmd[0] == 'L' and left_stack: 
        right_stack.append(left_stack.pop()) 
    elif cmd[0] == 'D' and right_stack: 
        left_stack.append(right_stack.pop()) 
    elif cmd[0] == 'B' and left_stack: 
        left_stack.pop() 
    elif cmd[0] == 'P': left_stack.append(cmd[2]) 
sys.stdout.write(''.join(left_stack + right_stack[::-1]))
'''
# 나도 그냥 sys로 해봄
# 아니 sys 떼면 안돼??? 대체 무슨 차이가 있다고 이게 안되지??? 어이털림;;
import sys
l_stack = list(sys.stdin.readline()[:-1])
m = int(sys.stdin.readline())
r_stack = list()
for i in range(m):
    command = sys.stdin.readline()
    if command[0] == 'P':
        l_stack.append(command[2])
    elif command[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif command[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif command[0] == 'B' and l_stack:
        l_stack.pop()
sys.stdout.write(''.join(l_stack+r_stack[::-1]))