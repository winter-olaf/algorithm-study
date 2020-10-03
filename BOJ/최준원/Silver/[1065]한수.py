n = int(input())
ans = 0
for i in range(1,n+1):
    if i <= 99:
        ans+=1
    elif i==1000:
        break
    else:
        o = i%10
        t = (i//10)%10
        h = i//100
        if (h-t) == (t-o):
            ans+=1
print(ans)