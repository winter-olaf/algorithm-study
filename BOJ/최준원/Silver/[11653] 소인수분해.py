N = int(input())

i = 2
while N >= 2:
    if N%i == 0:
        print(i)
        N //= i
    else:
        i += 1
