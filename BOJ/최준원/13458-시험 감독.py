n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

# 이게 안되는 이유가 뭘까. 이런 젠장 마지막에 pring(def)를 안했다고 틀린거였어? 어이가 없군
# 484ms
def solve(n,a,b,c):
    viewer = 0
    for i in range(n):
        if a[i] > 0:
            a[i] -= b
            viewer += 1
        if a[i] > 0:
            viewer += int(a[i]/c)
            if a[i] % c != 0:
                viewer += 1
    return viewer

# 492ms
import math
def solve(n,a,b,c):
    viewer = n
    for i in range(n):
        a[i] -= b
        if a[i] > 0:
            viewer += math.ceil(a[i]/c)
    return viewer
print(solve(n,a,b,c))

        
print(solve(5,[10,9,10,9,10],7,20))
print(solve(5,[10,9,10,9,10],7,2))
print(solve(5,[1000000,1000000,1000000,1000000,1000000],5,7))
print(solve(3,[3,4,5],2,2))


