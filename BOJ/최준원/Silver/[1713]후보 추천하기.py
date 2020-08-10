from sys import stdin
n = int(stdin.readline())
vote_count = int(stdin.readline())
votes = list(map(int,stdin.readline().split()))
stack = []

def isIn(stack, vs):
    for i in stack:
        if i[2] == vs:
            return True
    return False

for idx, v in enumerate(votes):
    # 스택 안에 그 수가 있다면
    if isIn(stack, v):
        for idxS, vs in enumerate(stack):
            # 그 학생의 투표 횟수 + 1
            if vs[2] == v:
                stack[idxS][0] += 1
                break
    else:
        if len(stack) < n:
            stack.append([1, idx, v])
        else:
            stack[0] = [1, idx, v]
    # 인덱스(오래된 순)으로 정렬
    stack.sort(key=lambda x: (x[0], x[1]))

stack.sort(key=lambda x: int(x[2]))
for i in range(n):
    if i == n-1:
        print(stack[i][2])
    else:
        print(stack[i][2], end=' ')