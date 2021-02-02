from sys import stdin

t = int(input())

for test_case in range(t):
    n = int(input())
    # data = list(map(int, stdin.readline().split()))
    data = list(map(int, input().split()))
    res = 0

    stack = []
    for i in range(len(data)):
        if i == len(data) - 1:
            res += ((data[i] * len(stack)) - sum(stack))
            break
        if data[i] <= data[i + 1]:
            stack.append(data[i])
        elif data[i] > data[i + 1]:
            res += ((data[i] * len(stack)) - sum(stack))
            stack = []

    # 어우.. 출력부분
    print('#{} {}'.format(test_case+1, res))

'''
1
3
3 5 9
'''
