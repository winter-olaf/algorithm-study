# import sys
#
# n,c = map(int,sys.stdin.readline().split())
# house = []
# for i in range(n):
#     house.append(int(sys.stdin.readline()))
#
# house = sorted(house)
#
# start = 1
# end = len(house)
# middle = 0
# midHouse = 0
# distances = []
#
# def searchMiddle(start,end):
#     midHouse = 0
#     midTemp = 0
#     for i in range(start,end):
#         temp = min(house[i] - house[0], house[-1] - house[i])
#         if midTemp < temp:
#             midHouse = i
#             midTemp = temp
#
#     return midHouse,midTemp
#
# if c==2:
#     print(house[-1] - house[0])
# else:
#     while c:
#         if midHouse !=0:
#             leftHouse,leftTemp = searchMiddle(start,midHouse)
#             rightHouse,rightTemp = searchMiddle(midHouse,end)
#             if (leftTemp < rightTemp):
#                 midHouse = rightHouse
#                 distances.append(rightTemp)
#             else:
#                 midHouse = leftHouse
#                 distances.append(leftTemp)
#             c -=1
#         else:
#             midHouse,midTemp = searchMiddle(start,end)
#             distances.append(midTemp)
#             c-=3
#
# print(min(distances))
# 역시 시간초과. 맞는지도 모르겠음

import sys


n, c = map(int, sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

min_gap = 1
max_gap = house[-1] - house[0]
result = 0

while (min_gap <= max_gap):
    gap = (min_gap + max_gap) // 2
    value = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= value + gap:
            value = house[i]
            count += 1
    if count >= c:
        min_gap = gap + 1
        result = gap
    else:
        max_gap = gap - 1


print(result)

#포인트는 거리를 이분탐색으로 잡았을 떄 가능한지 불가능한지 판단하는 것 이였다.