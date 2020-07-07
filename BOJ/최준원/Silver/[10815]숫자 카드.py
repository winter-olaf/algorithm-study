# 2초 / 256MB
# 시간 초과
# from sys import stdin,stdout
# n = int(stdin.readline())
# a = list(map(int,stdin.readline().split()))
# m = int(stdin.readline())
# b = list(map(int, stdin.readline().split()))
# for i in b:
#     print(1,end=' ') if i in a else print(0,end=' ')

# 다른 풀이를 보니 set으로 받은 사람들이 있던데 입력 조건에 두 숫자 카드에 같은 수가 적혀있는 경우는 없다고 했는데 뭐지...?
# 뭐지.....?? 통과 함. 
# 684ms / 119412KB
# from sys import stdin, stdout
# n = int(stdin.readline())
# a = set(map(int, stdin.readline().split()))
# m = int(stdin.readline())
# b = list(map(int, stdin.readline().split()))
# for i in b:
#     print(1,end=' ') if i in a else print(0,end=' ')

# 이분 탐색은 시간복잡도가 O(log n)
# 2708ms / 107364KB
from sys import stdin,stdout
n = int(stdin.readline())
a = sorted(list(map(int,stdin.readline().split())))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

def b_search(num):
    left = 0
    right = n-1
    while left<=right:
        mid = (left+right)//2
        if a[mid] == num: # 찾으면 1 리턴
            return 1
        elif a[mid] > num: # 상근이 카드의 중간값이 비교하는 숫자보다 크면 최소값을 높여서 비교하는 범위를 줄임
            right = mid-1 
        else:  # 상근이 카드의 중간값이 비교하는 숫자보다 작면 최대값을 낮춰서 비교하는 범위를 줄임
            left = mid+1
    # 끝까지 찾지 못하고 left가 right와 같거나 커지면 0 리턴
    return 0
for i in b:
    print(b_search(i),end=' ')