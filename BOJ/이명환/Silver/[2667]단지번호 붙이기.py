import sys

N = int(sys.stdin.readline())
index_N = N-1
matrix = [[int(block) for block in input()] for _ in range(N)]
global house
house = 0
whole_area = []
x, y = 0, 0

def divide_area(x, y):
    global house
    if matrix[x][y] == 1:
        matrix[x][y] =0
        house +=1
        # 하
        if x + 1 <= index_N and matrix[x + 1][y] == 1:
            divide_area(x + 1, y)
        # 상
        if x - 1 >= 0 and matrix[x - 1][y] == 1:
            divide_area(x - 1, y)
        # 좌
        if y - 1 >= 0 and matrix[x][y - 1] == 1:
            divide_area(x, y - 1)
        # 우
        if y + 1 <= index_N and matrix[x][y + 1] == 1:
            divide_area(x, y + 1)
    else:
        pass

while(True):
    if matrix[x][y] == 1:
        divide_area(x, y)
        if house != 0:
            whole_area.append(house)
            house=0
        else:
            pass
    y+=1
    if y== N:
        x+=1
        y=0
    if x == N:
        break

print(len(whole_area))
for i in sorted(whole_area):
    print(i)