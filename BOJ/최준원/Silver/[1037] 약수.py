N = int(input())
data = list(map(int, input().split()))
data = sorted(data)
print(data[0] * data[-1])