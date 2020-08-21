import sys

n = int(sys.stdin.readline())
triangle = []
for i in range(n):
    triangle.append(list(map(int,list(sys.stdin.readline().split()))))
for row in range(n-1,0,-1):
    for idx in range(len(triangle[row - 1])):
        triangle[row - 1][idx] = max(triangle[row-1][idx] + triangle[row][idx], triangle[row-1][idx]+ triangle[row][idx+1])
print(triangle[0][0])