import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
max_num = arr[0]
current_sum = 0
for i in arr:
    current_sum += i
    if current_sum > max_num:
        max_num = current_sum
    if current_sum <0:
        current_sum =0
print(max_num)