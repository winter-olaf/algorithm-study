import sys
import itertools

n = int(sys.stdin.readline())

stat = [ list(map(int,sys.stdin.readline().split())) for i in range(n)]
team = [ i for i in range(n)]
startLink_team = list(itertools.combinations(team,int(n/2)))
#start 처음 부터 n/2까지 link 맨끝부터 n/2 +1 까지
start_team = startLink_team[:len(startLink_team)//2]
link_team = startLink_team[len(startLink_team)//2:]
link_team = link_team[::-1]

min = 100*n*n
for i,j in zip(start_team,link_team):
    temp1 = 0
    temp2 = 0
    for m in i:
        for n in i:
            temp1+= stat[m][n]
    for m in j:
        for n in j:
            temp2 += stat[m][n]
    if abs(temp1 - temp2) < min:
        min = abs(temp1 - temp2)
print(min)
#맞긴한데 시간이 엄청걸린다 비효율적으로 풀었나..?