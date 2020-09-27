from sys import stdin, stdout
t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    res = 0
    turn = True
    while n>0:
        if turn:
            if n%2==0:
                res+=n//2
                n//=2
            else:
                res+=1
                n-=1
            turn = False
        else:
            if n%2==0:
                n//=2
            else:
                n-=1
            turn = True
    print(res)