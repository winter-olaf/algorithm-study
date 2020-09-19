import time
# 숫자 카드 게임

start = time.time()
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))

    # min 함수 사용
    # min_val = min(data)
    # result = max(min_val, result)

    # 2중 for문 사용
    min_val = 10001 # 10000까지이므로, 10001으로 초기화
    for i in data:
        min_val = min(i, min_val) # 각 배열의 최소값 빼기
    result = max(min_val, result) # 가장 작은 수들 중 가장 큰 수 출력
print(result)
print("소요 시간 : ", time.time() - start)