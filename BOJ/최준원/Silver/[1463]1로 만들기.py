# 무식한 완탐
'''
n = int(input())
result = 0
while n>1:
    if n%3==0:
        n//=3
        result+=1
        print(n)
    elif (n-1)%3==0:
        n = (n-1)//3
        result+=2
        print(n)
    elif n%2==0:
        n//=2
        result+=1
        print(n)
    else:
        n-=1
        result+=1
        print(n)
print(result)
'''
# min 함수의 이용
n = int(input())
result = 0
minimum = [n]
def to_one(arr):
    tmp = []
    for i in arr:
        tmp.append(i-1)
        if i%3 == 0:
            tmp.append(i//3)
        if i%2 == 0:
            tmp.append(i//2)
    return tmp
while True:
    if n==1:
        print(0)
        break
    tmp = minimum[:]
    minumum = []
    minimum = to_one(tmp)
    result+=1
    if min(minimum) == 1:
        print(result)
        break