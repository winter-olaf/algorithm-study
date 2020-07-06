# import sys
#
# n = int(sys.stdin.readline())
# street = []
# for i in range(n):
#     k = int(sys.stdin.readline())
#     street.append(k)
# interval = []
# for i in range(len(street)-1):
#     a = street[i+1] - street[i]
#     interval.append(a)
# def gcd_(a,b):
#     while b>0:
#         a,b = b,a%b
#     return a
# def gcd_N(arr):
#     gcd = arr[0]
#     for item in arr:
#         gcd = gcd_(gcd,item)
#     return gcd
# gcd_interval = gcd_N(interval)
#
# new_tree = street[0]
# answer = 1
# while(new_tree < street[-1]):
#     new_tree+= gcd_interval
#     answer +=1
# answer -= len(street)
# print(answer)
# 시간초과

import sys

n = int(sys.stdin.readline())
street = []
for i in range(n):
    k = int(sys.stdin.readline())
    street.append(k)
interval = []
street = sorted(street)
for i in range(len(street)-1):
    a = street[i+1] - street[i]
    interval.append(a)

def gcd_(a,b):
    while b>0:
        a,b = b,a%b
    return a
def gcd_N(arr):
    gcd = arr[0]
    for item in arr:
        gcd = gcd_(gcd,item)
    return gcd
gcd_interval = gcd_N(interval)

answer = (street[-1] - street[0])/gcd_interval +1 - len(street)
print(int(answer))