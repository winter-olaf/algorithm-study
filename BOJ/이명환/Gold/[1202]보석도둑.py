# import sys
#
# M,K = map(int,sys.stdin.readline().split())
# jewels = []
#
# def discern(weight,price):
#     start = 0
#     end = len(jewels) -1
#     ret = len(jewels) -1
#
#     while(start<end-1):
#         mid = start+end//2
#         je_weight,je_price = jewels[mid]
#
#         if je_weight > weight:
#             weight_gap = je_weight -weight
#             price_gap = je_price -(price + weight*weight_gap)
#         elif je_weight < weight:
#             weight_gap = weight - je_weight
#             price_gap = (je_price+je_price*weight_gap) - price
#         else:
#             price_gap = je_price - price
#
#         if price_gap >0: #우선순위가 jewels[mid]보다 높을 떄
#             start = mid+1
#             ret = mid
#         else: #우선순위가 jewels[mid]보다 낮을 떄
#             end = mid - 1
#
#     jewels.insert(ret,(weight,price))
#
# for i in range(M):
#     weight, price = map(int,sys.stdin.readline().split())
#     discern(weight,price)
#     print(jewels)
import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
gem = []
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, [weight, value])

bag = []
for _ in range(K):
    capacity = int(sys.stdin.readline())
    heapq.heappush(bag, capacity)

total_value = 0  # 답이 될 숫자
capable_gem = []  # 현재 bag의 capacity보다 작은 모든 보석들

for _ in range(K):
    capacity = heapq.heappop(bag)  # Bag의 최솟값을 heappop 해준다. 해당 Bag은 현재의 capacity 즉, 수용량이 된다

    while gem and capacity >= gem[0][0]:  # 현재 bag의 capacity보다 이하인 모든 보석에 관하여
        [weight, value] = heapq.heappop(gem)  # 최소 무게부터 차례대로 꺼낸다
        heapq.heappush(capable_gem, -value)  # 무게를 제외한 값만 heappush하여 넣어준다(최대힙 구성)

    if capable_gem:  # gem 최소보다는 작지만 넣을 수 있는 보석들은 있는 경우
        total_value -= heapq.heappop(capable_gem)
    elif not gem:  # 남은 보석이 한 개도 없는 경우
        break

print(total_value)
#아니 문제를 잘못읽었다.. 가방에 남는 공간에 들어갈 수 있는 보석들을 전부 넣어 최댓값을 구하는줄
#알았는데 알고보니 하나만 넣으면 된다..................whyrano