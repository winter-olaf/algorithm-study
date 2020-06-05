import sys
n = int(sys.stdin.readline())
data =sorted(list(map(int,sys.stdin.readline().split())))

def binary_search(target):
    idx = 0
    end = len(data) -1
    while idx <= end:
        mid = (idx + end) //2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            idx = mid + 1
        elif data[mid] > target:
            end = mid -1
    return 0

m = int(sys.stdin.readline())
for num in list(map(int,sys.stdin.readline().split())):
    print(binary_search(num,),end=' ')