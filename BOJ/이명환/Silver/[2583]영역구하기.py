import sys
from  collections import deque
m,n,k = map(int,sys.stdin.readline().split())
graphPaper =[[0]*n for i in range(m)]
visited = [[False]*n for _ in range(m)]
ydir = [-1,1,0,0]
xdir = [0,0,-1,1]
for i in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    y1 = m-y1-1
    x2 = x2-1
    y2 = m-y2
    gap = (abs(x1-x2) , abs(y1-y2))
    if gap[0] and gap[1]:
        for row in range(gap[1]+1):
            for column in range(gap[0]+1):
                graphPaper[y2+row][x1+column] = 1
    elif gap[0]:
        for column in range(gap[0] + 1):
            graphPaper[y2][x1 + column] = 1
    elif gap[1]:
        for row in range(gap[1]+1):
            graphPaper[y2+row][x1] = 1
q = deque([])
flag = False

cnt = 0
extent = []
for r in range(m):
    for c in range(n):
        if graphPaper[r][c] ==0 and visited[r][c] == False:
            q.append((r,c))
            cnt+=1
            visited[r][c] = True
            flag = True
            break
    if flag:
        break

while(q):
    flag = False
    row,column = q.popleft()

    for i in range(4):
        y = ydir[i] + row
        x = xdir[i] + column
        if 0<=x<=n-1 and 0<=y<=m-1 and visited[y][x] == False:
            if graphPaper[y][x] == 0:
                visited[y][x] = True
                q.append((y,x))
                cnt+=1
    if q:
        pass
    else:
        extent.append(cnt)
        cnt =0
        for r in range(m):
            for c in range(n):
                if graphPaper[r][c] == 0 and visited[r][c] == False:
                    visited[r][c] = True
                    cnt+=1
                    q.append((r, c))
                    flag = True
                    break
            if flag:
                break
print(len(extent))
for i in sorted(extent):
    print(i,end=' ')
#  50%에서 틀렸다. 생각을 잘못했나. 다른방법을 강구해야할듯 이렇게 설계하는건 너무 번잡한 느낌..