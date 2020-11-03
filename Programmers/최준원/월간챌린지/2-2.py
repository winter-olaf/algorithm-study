result = []
def quad(x,y,x1,y1,n,arr):
    global result
    if n == 1:
        return arr[y][x]
    a = n//2

    r1 = quad(x,y,x+a,y+a,a, arr)
    r2 = quad(x+a,y,x+n,y+a,a, arr)
    r3 = quad(x,y+a,x+a,y+n,a, arr)
    r4 = quad(x+a,y+a,x+n,y+n,a, arr)

    if r1==r2==r3==r4 and len(str(r1))==1:
        return str(r1)
    else:
        return str(r1)+str(r2)+str(r3)+str(r4)

def solution(arr):
    N = len(arr)
    result = quad(0,0,N,N,N,arr)
    zero, one = 0,0
    print(result)
    for i in result:
        if i=='0':
            zero+=1
        else:
            one+=1
    print([zero,one])
    return [zero, one]    

solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
