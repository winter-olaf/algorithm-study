from sys import stdin
n = int(input())
towers = list(map(int, stdin.readline().split()))

tower_max = 0
idx_max = 0
result = []

for idx, val in enumerate(towers):
    # 만약 높이가 같을 경우에는 받을 수 없다고 가정함. 그냥 index만 건너뛰기
    if val >= tower_max:
        tower_max = val
        idx_max = idx
`
    elif val < tower_max:



'''tc
5
6 9 5 7 4
'''