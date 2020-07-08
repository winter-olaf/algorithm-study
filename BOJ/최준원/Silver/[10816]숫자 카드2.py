# 992ms / 108620KB
# from sys import stdin
# n = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))
# m = int(stdin.readline())
# b = list(map(int, stdin.readline().split()))
# cards = {}
# for i in a:
#     if i in cards:
#         cards[i] += 1
#     else:
#         cards[i] = 1
# for i in b:
#     if i in cards:
#         if i == b[-1]:
#             print(cards[i])
#         else:
#             print(cards[i],end=' ')
#     else:
#         print(0,end=' ')


# 788ms / 140972KB
# 백준 print 값을 어떻게 해야 하는지 확실히 알겠다. 마지막 Blank 하나정도는 봐준다.
from sys import stdin
from collections import Counter
n = int(stdin.readline())
a = stdin.readline().split()
m = int(stdin.readline())
b = stdin.readline().split()
ac = Counter(a)
for i in b:
    print(ac[i],end=' ') if i in ac else print('0',end=' ')