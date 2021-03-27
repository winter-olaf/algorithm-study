s = input()
t = input()

res = 0
while len(s) <= len(t):
    if s == t:
        res = 1
        break
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1][::-1]
print(res)