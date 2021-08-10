import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())
fireball_info = deque([])
dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]


for i in range(m):
    r,c,m,s,d = map(int,sys.stdin.readline().split())
    fireball_info.append((r,c,m,s,d))



for i in range(k):
    cnt = 0
    moved_fireball = deque([])
    fireball_location = [[[] for colmn in range(n + 1)] for row in range(n + 1)]
    while(fireball_info):
        r, c, m, s, d = fireball_info.popleft()
        nr = (r + s*dy[d])
        nc = (c + s*dx[d])

        if nr <1:
            nr = n - abs(nr)%n
        elif nr >n:
            nr = nr%n
            if nr ==0:
                nr = n
        if nc <1:
            nc = n - abs(nc)%n
        elif nc >n:
            nc = nc%n
            if nc ==0:
                nc =n

        fireball_location[nr][nc].append(cnt)
        moved_fireball.append((nr,nc,m,s,d))


        cnt+=1



    for row in range(1,n+1):
        for colmn in range(1,n+1):
            if fireball_location[row][colmn]:
                m,s,d =0,0,0
                verify_d = set()
                if len(fireball_location[row][colmn]) >=2:
                    for k in range(len(fireball_location[row][colmn])):
                        kr,kc,km,ks,kd = moved_fireball[fireball_location[row][colmn][k]]
                        m += km
                        s += ks
                        verify_d.add(kd%2)

                    m = int(m/5)
                    s = int(s/len(fireball_location[row][colmn]))
                    if m == 0:
                        continue
                    if len(verify_d) ==2:
                        for direct in range(1,8,2):
                            fireball_info.append((row,colmn,m,s,direct))
                    else:
                        for direct in range(0,7,2):
                            fireball_info.append((row,colmn,m,s,direct))
                else:
                    fireball_info.append(moved_fireball[fireball_location[row][colmn][0]])

ans= 0
while(fireball_info):
    r, c, m, s, d = fireball_info.popleft()
    ans += m

print(ans)












