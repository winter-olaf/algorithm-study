from collections import deque
n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0] * (2*n))
k_cnt = 0

while k_cnt < k:
    
