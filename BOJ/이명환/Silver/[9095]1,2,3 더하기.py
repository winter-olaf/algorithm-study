import sys

testcase = int(sys.stdin.readline())

def expression(x,n):
    global result
    for i in range(1,4):
        if x+i < n:
            expression(x+i,n)
        elif x+i == n:
            result +=1
        else:
            break
for i in range (testcase):
    n = int(sys.stdin.readline())
    result = 0
    expression(0,n)
    print(result)

