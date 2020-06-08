import sys
n= int(sys.stdin.readline().rstrip('\n'))
k = list(map(int,sys.stdin.readline().split()))
ans = 0
for i in k:
    flag = True
    es_prime = 1
    if i ==0 or i ==1:
        flag = False
    if flag:
        while(True):
            es_prime+=1
            if es_prime == i:
                ans +=1
                break
            elif i% es_prime == 0:
                break
print(ans)
#20200606