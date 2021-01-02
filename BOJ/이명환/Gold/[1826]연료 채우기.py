import sys
from collections import deque

N = int(sys.stdin.readline())
gas_station = []
passed = []
answer = 0

for i in range(N):
    dis,gas = map(int,sys.stdin.readline().split())
    gas_station.append((dis,gas))

L,P = map(int,sys.stdin.readline().split())
gas_station = deque(sorted(gas_station))
move = 0

while(move<L):
    if gas_station:
        d, g = gas_station.popleft()
        P -= d - move
        move += d - move
    else:
        g = 0
        P -= L-move
        move = L
    if(P<0):
        while(P<0):
            if passed:
                maxG = max(passed)
                passed.remove(maxG)
                P += maxG
                answer +=1
            else:
                move = L
                answer = -1
                break

    passed.append(g)
print(answer)
