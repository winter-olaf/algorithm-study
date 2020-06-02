import sys
n = int(sys.stdin.readline())
a_list = sorted(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = (list(map(int,sys.stdin.readline().split())))

def binary_search(target,data):
    start = 0
    end = len(data) -1
    while start <= end:
        mid = (start +end) //2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return False

for i in m_list:
    if binary_search(i,a_list):
        print('1')
    else:
        print('0')