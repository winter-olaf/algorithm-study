T = int(input())

for tc in range(1, T+1):
    num, cnt = input().split()
    N = len(num)
    res = [0] * N

    for i in range(N):
        res[i] = num[i]

    ch = 0
    idx = 0
    # 내림차순 정렬 되기 전까지 반복문 돌리기
    while res != res[::-1]:
        print(res)
        change_diff = 0
        tmp_change_stack = []
        change_stack = []
        if idx > N or ch >= int(cnt):
            break

        for i in range(idx+1, N):
            if int(res[idx]) <= int(res[i]):
                tmp_change_stack.append(i)
            else:
                # 자기보다 작은 수가 있으면 격리값을 1 추가한다
                # 격리값이 있고 최대값에 중복이 있다면,
                # 최대값의 중복수
                change_diff += 1
        print('tmp ', tmp_change_stack)
        for i in range(len(tmp_change_stack)):
            if res[tmp_change_stack[i]] >= res[tmp_change_stack[-1]]:
                change_stack.append(tmp_change_stack[i])

        print(res, change_stack, change_diff)

        if change_diff and len(change_stack) >= 2 and ch >= 2:
            diff_idx = min(change_diff, len(change_stack), ch-1)
            res[idx], res[change_stack[-diff_idx]] = res[change_stack[-diff_idx]], res[idx]
            ch += 1
        elif change_stack:
            res[idx], res[change_stack[-1]] = res[change_stack[-1]], res[idx]
            ch += 1

        idx += 1

    dup_idx = 0
    for i in range(N - 1):
        if res[i] == res[i + 1]:
            dup_idx += 1
            break

    # print(ch, dup_idx, res)

    while ch < int(cnt):
        if dup_idx:
            ch += 1
        else:
            res[-2], res[-1] = res[-1], res[-2]
            ch += 1

    print("".join(res))
#
# 987456 - 3
# 987654
# 987645
# 987654

# 82838
# 32678
# 321888888, 1
# 88832








