# n,m = map(int,(input().split()))
#
# def max_common_divisor(n,m):
#     max_div = 1
#     k=2
#     a = min(n,m)
#     while(k<=a):
#         if n%k == 0 and m%k ==0:
#             max_div = k
#         k+=1
#     return max_div
#
# def the_least_common_multiple(n,m):
#     k = max(n,m)
#     while(True):
#         if k%n == 0 and k%m == 0:
#             return k
#         k+=1
#
# print(max_common_divisor(n,m))
# print(the_least_common_multiple(n,m))
# #20200606
# 재채점 후 시간초과

n,m = map(int,(input().split()))

def max_common_divisor(n,m):
    while(m):
        n,m = m,n%m
    return n

def the_least_common_multiple(n,m):
    return (n*m)//max_common_divisor(n,m)

print(max_common_divisor(n,m))
print(the_least_common_multiple(n,m))
#유클리드 호제법 사용