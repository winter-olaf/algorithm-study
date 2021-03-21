def star(i, j, n):
    if (i//n)%3 == 1 and (j//n)%3 == 1: # 재귀적으로 가져온 n으로 나눈
        print(' ', end='') # 빈 공간이어야 하는 곳이라면
    else:
        if n//3 == 0:
            print('*', end='')
        else:
            star(i, j, n//3)

n = int(input())

for i in range(n):
    for j in range(n):
        star(i, j, n)
    print()
