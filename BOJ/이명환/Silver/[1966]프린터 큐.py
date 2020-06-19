import sys
from collections import deque
testcase = int(sys.stdin.readline())
for i in range(testcase):
    condition = list(map(int,sys.stdin.readline().split()))
    m = condition[1]
    doc = list(map(int,sys.stdin.readline().split()))
    printer = deque(doc)
    cnt = 0
    while(m >-1):
        if (printer[0]< max(printer)):
            temp = printer.popleft()
            if (m == 0):
                printer.append(temp)
                m += len(printer) - 1
            else:
                printer.append(temp)
                m -= 1
        else:
            cnt +=1
            temp = printer.popleft()
            if (m == 0):
                m-=1
                print(cnt)
            else:
                m-=1
