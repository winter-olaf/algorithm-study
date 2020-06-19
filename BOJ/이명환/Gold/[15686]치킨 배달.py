import sys
n_m = list(map(int,sys.stdin.readline().split()))
city = []
for i in range(n_m[0]):
    city.append(list(map(list,sys.stdin.readline().split())))
city = sum(city,[])
chicken = []
home = []
idx = 0
print(city)
while(idx<n_m[0]**2):
    temp = idx +5
    if city[idx][0] == '2':
        chicken.append((temp//n_m[0],temp%n_m[0]+1))
    elif city[idx][0] == '1':
        home.append((temp//n_m[0],temp%n_m[0]+1))
    idx +=1
print(chicken)
print(home)