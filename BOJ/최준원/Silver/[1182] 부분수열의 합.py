from sys import stdin
N, S = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))
selected = [0] * N
res = 0

def power_set(idx):
    global res
    if idx == N:
        tmp = 0
        # 크기가 양수인 부분수열
        if not max(selected):
            return

        for i in range(N):
            if selected[i]:
                tmp += data[i]
        if tmp == S:
            res += 1
        return

    selected[idx] = 1
    power_set(idx + 1)
    selected[idx] = 0
    power_set(idx + 1)

power_set(0)
print(res)