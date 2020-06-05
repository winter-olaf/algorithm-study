import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    instruction  =(sys.stdin.readline().split())
    if instruction[0] == 'push':
        stack.append(instruction[1])
    elif instruction[0] == 'pop':
        if stack:
            print(stack.pop(-1))
        else:
            print('-1')
    elif instruction[0] == 'size':
        print(len(stack))
    elif instruction[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    elif instruction[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
#내 pycharm 에서 돌리면 결과가 이상하게 나오는데, 백준에서는 또 맞다고 뜬다.. 무슨일이고