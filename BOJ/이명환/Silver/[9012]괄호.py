import sys
n = int(sys.stdin.readline())
for i in range(n):
    data = sys.stdin.readline().split()
    count = 0
    is_right = True
    if data[0][0] == ')':
        print('NO')
        continue
    for k in data[0]:
        if k == '(':
            count +=1
        else:
            count -=1
            open = False
        if count < 0:
            is_right = False
            break

    if is_right and count == 0:
        print('YES')
    else:
        print('NO')

