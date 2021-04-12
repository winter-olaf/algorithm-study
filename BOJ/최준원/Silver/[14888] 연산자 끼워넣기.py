from itertools import permutations
max_val = -1000000001
min_val = 1000000001

N = int(input())
data = list(map(int, input().split()))
# + - x //
data2 = list(map(int, input().split()))

oper = []
for i in range(4):
    for j in range(data2[i]):
        oper.append(i)

perm = list(permutations(oper, N-1))

for comb in perm:
    tmp = data[0]

    for i in range(0, N-1):
        if comb[i] == 0:
            tmp += data[i+1]
        elif comb[i] == 1:
            tmp -= data[i+1]
        elif comb[i] == 2:
            tmp *= data[i+1]
        elif comb[i] == 3:
            if tmp < 0:
                tmp = -(-tmp//data[i+1])
            else:
                tmp //= data[i+1]

    if tmp > max_val:
        max_val = tmp
    if tmp < min_val:
        min_val = tmp

print(max_val)
print(min_val)