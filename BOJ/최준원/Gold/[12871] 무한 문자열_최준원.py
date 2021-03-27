s = input()
t = input()

def infinite(a,b):
    ss = a * len(b)
    tt = b * len(a)
    if ss == tt:
        return 1
    return 0

if len(s) < len(t):
    print(infinite(s, t))
else:
    print(infinite(t, s))