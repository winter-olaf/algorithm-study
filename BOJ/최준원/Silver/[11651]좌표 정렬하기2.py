# 응? 왜 틀렸지?
# from sys import stdin
# n = int(stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(stdin.readline().split())
# for a,b in sorted(arr,key=lambda x:x[1]):
#     print(a,b)

# 음... 뭐가 문제일까.
# from sys import stdin
# n = int(stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(stdin.readline().split())
# for a,b in sorted(arr,key=lambda x:(x[1],x[0])):
#     print(a,b)

# 악 바보같이 정수로 받는걸 깜빡했다
# 시험삼아 람다 조건의 x[0]을 빼 봤는데, 오답으로 된다. 정렬 조건을 하나하나 지정해 줘야 함.

# 392ms / 55156KB
from sys import stdin
n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,stdin.readline().split())))
for a, b in sorted(arr, key=lambda x: (x[1], x[0])):
    print(a, b)