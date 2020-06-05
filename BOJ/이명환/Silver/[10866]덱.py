import sys
from collections import deque
n = int(sys.stdin.readline())
deq = deque()
for i in range(n):
    instruction  =(sys.stdin.readline().split())
    if instruction[0] == 'push_front':
        deq.appendleft(instruction[1])
    elif instruction[0] == 'push_back':
        deq.append(instruction[1])
    elif instruction[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print('-1')
    elif instruction[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print('-1')
    elif instruction[0] == 'size':
        print(len(deq))
    elif instruction[0] == 'empty':
        if deq:
            print('0')
        else:
            print('1')
    elif instruction[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print('-1')
    elif instruction[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print('-1')