# 시간초과
'''
완탐은 시간초과가 난다.
from sys import stdin
t = int(input())
for _ in range(t):
    n = int(input())
    numbers, flag = [], False
    for i in range(n):
        numbers.append(stdin.readline().strip())
    for i in range(n):
        data = numbers[:i] + numbers[i+1:]
        for j in data:
            if j.startswith(numbers[i]):
                flag = True
    if flag == True:
        print('NO')
    else:
        print('YES')
'''
# 정렬하면 앞뒤만 비교하면 된다
# return으로만 처리하면 백준은 에러 뜸. 함수를 쓸 때는 print하고 return 처리를 해 줘야 함
from sys import stdin
def check(numbers):
    for i in range(len(numbers)-1):
        if numbers[i+1].startswith(numbers[i]):
        # if numbers[i] == numbers[i+1][:len(numbers[i])]:
            print('NO')
            return
    print('YES')

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(stdin.readline().strip())
    numbers.sort()
    check(numbers)
'''
124,225,227,22534를 정렬한 결과
124, 225, 22534, 227
'''