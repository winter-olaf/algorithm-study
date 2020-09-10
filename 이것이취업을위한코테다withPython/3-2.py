n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
first = nums[-1]
second = nums[-2]

result = 0