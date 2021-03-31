N = int(input())

selected = [0] * N
rome = [1, 5, 10, 50]
res = set()

def comb(idx, cnt, num):
    global res
    if idx == N:
        res.add(num)
        return
    # Backtracking
    # 반복문 돌릴때
    # i가 0으로 재귀 들어가면 i의 범위는 0~3
    # 같은 깊이에서 i가 1로 들어가면 반복 범위는 1~3, 2~3, 3
    # 만약 그냥 4로 해 두면 0~3, 0~3, 0~3, 0~3을 반복할 것이다
    for i in range(cnt, 4):
        num += rome[i]
        comb(idx+1, i, num)
        num -= rome[i]

comb(0, 0, 0)
print(len(res))