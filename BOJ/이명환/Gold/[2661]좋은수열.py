import sys

n = int(sys.stdin.readline())

def right_arr(arr,l):
    for i in range(1,l//2 +1):
        discri1 = arr[l-i:]
        discri2 = arr[l-2*i:l-i]
        if discri1 == discri2:
            return False
    if l == n:
        print(arr)
        sys.exit()
    else:
        for i in ['1','2','3']:
            right_arr(arr+i,l+1)
right_arr('1',1)