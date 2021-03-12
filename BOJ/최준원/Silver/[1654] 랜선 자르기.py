from sys import stdin
K, N = map(int, stdin.readline().split())
data = [int(stdin.readline()) for x in range(K)]

low = 1
high = max(data)

while low <= high:
    # 중간값을 도출한 뒤, 중간값으로 data를 연산한 결과(tmp)가
    # N보다 크다면 나눈 수가 작다는 것이니 더 키워본다.
    # N보다 작다면 나눈 수가 크다는 것이니 더 작은 범위로 간다.

    # 만약 N개로 자를 수 있었더라도, '최대값'을 찾아야 하기 때문에 끝까지 간다.
    # high 값이 변동되었을 때에 답을 리턴해야 하므로 mid값은 결과값 한 턴 전의 값이 되어버린다.
    mid = (low+high)//2
    tmp = 0
    for i in data:
        tmp += i//mid

    if tmp >= N:
        low = mid + 1
    elif tmp < N:
        high = mid - 1

# 여기서 자꾸 mid 값을 리턴해서 틀렸었다.
print(high)