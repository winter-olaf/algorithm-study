n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
first = nums[-1]
second = nums[-2]
# 머리를 좀 쓴 풀이
result = 0 
count = (m//(k+1))*k + m%(k+1)

result += count * first
result += (m - count) * second

print(result)
# 단순한 풀이
'''
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result+=first
        m-=1
    if m == 0:
        break
    result+=second
    m-=1
print(result)
'''
