import sys
import heapq

n= int(sys.stdin.readline())
card_bundle = []
card_combine = []

for i in range(n):
    x = int(sys.stdin.readline())
    heapq.heappush(card_bundle,x)

if len(card_bundle) ==1 :
    print(0)
else:
    result = 0
    while(len(card_bundle)>1):
        temp1 = heapq.heappop(card_bundle)
        temp2 = heapq.heappop(card_bundle)
        result += temp1 + temp2
        heapq.heappush(card_bundle,temp1+temp2)
    print(result)

#heap