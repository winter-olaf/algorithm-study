T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = 0
    cal = arr[:]

    for i in range(N-1):
        if cal == sorted(arr):
            res += N-i-1
            break
        j = cal.index(min(cal[i:]))
        cal = cal[:i] + cal[i:j+1][::-1] + cal[j+1:]
        cost = j - i + 1
        res += cost

    print("Case #{}: {}".format(tc, res))
