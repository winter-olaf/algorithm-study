import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    instruction  =(sys.stdin.readline().split())
    if instruction[0] == 'push':
        queue.append(instruction[1])
    elif instruction[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print('-1')
    elif instruction[0] == 'size':
        print(len(queue))
    elif instruction[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif instruction[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    elif instruction[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print('-1')

#순수 queue.Queue()로도 풀어볼까 했는데 q[0], q[1] ,q[-1]처럼 인덱싱이 안되네..;