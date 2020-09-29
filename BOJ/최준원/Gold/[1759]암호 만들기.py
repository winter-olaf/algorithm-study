l, c = map(int,input().split())
pw = list(map(str,input().split()))
pw.sort()
password = []
wantam = []
# L자리의 암호를 얻기 위한 dfs
def dfs(depth, index, l, c):
    if depth == l:
        wantam.append(''.join(password))
        return
    for i in range(index, c):
        password.append(pw[i])
        dfs(depth+1, i+1, l, c)
        password.pop()

def solution(arr):
    for i in arr:
        vows = 0
        cons = 0
        for j in i:
            if j in 'aeiou':
                vows += 1
            else:
                cons += 1
        if vows>=1 and cons>=2:
            print(i)
    return
dfs(0,0,l,c)
solution(wantam)