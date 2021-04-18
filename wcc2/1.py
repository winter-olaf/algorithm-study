def solution(absolutes, signs):
    res = 0
    for a,b in zip(absolutes, signs):
        if b:
            res += a
        else:
            res -= a
    return res