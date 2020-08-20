import sys
from collections import deque

N = int(sys.stdin.readline())
oper_table = [0]*(N+1)
q = deque([N])
while(q):
    v = q.popleft()
    if v == 1:
        print(oper_table[v])
        break
    if v %3 == 0 and oper_table[int(v/3)] == 0:
        temp = int(v/3)
        q.append(temp)
        oper_table[temp] = oper_table[v] +1
    if v %2 == 0 and oper_table[int(v/2)] ==0 :
        temp = int(v/2)
        q.append(temp)
        oper_table[temp] = oper_table[v] +1
    if oper_table[v-1] ==0:
        temp = int(v-1)
        q.append(temp)
        oper_table[temp] = oper_table[v] +1