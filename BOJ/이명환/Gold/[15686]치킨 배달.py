import sys
from itertools import combinations
n_m = list(map(int,sys.stdin.readline().split()))
city = []
for i in range(n_m[0]):
    city.append(list(map(list,sys.stdin.readline().split())))
city = sum(city,[])
chicken = []
home = []
idx = 0
while(idx<n_m[0]**2):
    temp = idx +n_m[0]
    if city[idx][0] == '2':
        chicken.append((temp//n_m[0],temp%n_m[0]+1))
    elif city[idx][0] == '1':
        home.append((temp//n_m[0],temp%n_m[0]+1))
    idx +=1
chicken = list(combinations(chicken,n_m[1]))
#예상치 못하게 list안 tuple 형태의 원소들은 조합이 안되는 것 같다.. 방법을 강구하자
#조합이 된다 예제에서 M이 현재 치킨집 개수랑 같아서 조합이 안된 것 처럼 보였다.. 나 바보인듯
total_distance = n_m[0]**3
for k in chicken:
    total_temp = 0
    for i in home:
        distance = n_m[0]**2
        temp = 0
        for j in k:
            h_x,h_y = i
            c_x,c_y = j
            temp = abs(h_x-c_x) + abs(h_y-c_y)
            if temp < distance:distance=temp
        total_temp += distance
    if total_temp < total_distance:total_distance = total_temp
print(total_distance)