N=int(input())
result = []
def divtwo(x):
    for i in range(x//2):
        result.append(2)
    x = x/(x//2)
    return x
def divThree(x):
    for i in range(N//3):
        result.append(3)
    x = x/(x//3)
    return x
while True:
    if N < 2:
        break
    if N%2 == 0:
        divtwo(N)
    elif N%3 == 0:
        divThree(N)
print(result)