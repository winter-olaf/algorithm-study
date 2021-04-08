s, e = map(int, input().split())
sq_check = [1] * (e-s+1)

i = 1
cnt = 0

while i*i <= e:
    i += 1
    square = i*i
    start = s//square

    while square*start <= e:
        idx = square*start - s
        if idx >= 0 and sq_check[idx]:
            sq_check[idx] = 0
            cnt += 1
        start += 1

print(len(sq_check) - cnt)