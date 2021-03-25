from sys import stdin
A, B = map(int, stdin.readline().split())

res = 1
while B != A:
    if B < A or B%10 != 1 and B%2 != 0:
        res = -1
        break
    else:
        if B%10 == 1:
            B //= 10
            res += 1
        else:
            B //= 2
            res += 1
print(res)