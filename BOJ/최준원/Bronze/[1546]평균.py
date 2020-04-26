n = int(input())
score = list(map(int,input().split()))
res = 0
for i in score:
    res += i/max(score)*100
ans = res/n
print(ans)