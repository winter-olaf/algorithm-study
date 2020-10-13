# 0.5s Time limit
n, x, y = int(input()), 0, 0
while n>0:
    n-=x
    x+=1
    if n<=x:
        y=n
        break
son = x

if x%2==0:
    print(x+'/'+y)