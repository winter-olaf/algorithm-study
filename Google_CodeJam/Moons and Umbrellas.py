T = int(input())

for tc in range(1, T+1):
    X, Y, S = map(str, input().split())
    prev = S[0]
    res = 0

    for idx in range(1, len(S)):
        if S[idx] == prev:
            continue
        elif S[idx] == '?':
            S[idx] = prev
        else:
            if
            prev = S[idx]
