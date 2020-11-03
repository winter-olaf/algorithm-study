n = int(input())
matrix = [input() for x in range(n)]

def quad(x,y,xx,yy,n):
    if n==1:
        return matrix[y][x]
    a = n//2
    r1 = quad(x,y,xx+a,yy+a,a)
    r2 = quad(x+a,y,xx+n,yy+a,a)
    r3 = quad(x,y+a,xx+a,yy+n,a)
    r4 = quad(x+a,y+a,xx+n,yy+n,a)

    if r1==r2==r3==r4 and len(r1)==1:
        return r1
    else:
        return '('+r1+r2+r3+r4+')'
print(quad(0,0,n,n,n))