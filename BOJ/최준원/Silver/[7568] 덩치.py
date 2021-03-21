N = int(input())

data = [list(map(int, input().split())) for x in range(N)]
grade = [0] * N

for i in range(N):
    tmp = 1
    equal = 0
    tmp_list = data[:i] + data[i+1:]
    i_w, i_h = data[i][0], data[i][1]
    for j in tmp_list:
        # 비교했을 때, 둘 다 작을 때
        j_w, j_h = j[0], j[1]
        if j_w > i_w and j_h > i_h:
            tmp += 1
    grade[i] = tmp

print(*grade)
