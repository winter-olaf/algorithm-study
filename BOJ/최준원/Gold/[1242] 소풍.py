# from collections import deque
# N, K, M = map(int, input().split())
#
# queue = deque([x for x in range(1, N+1)])
#
# cnt = 1
# out = 0
#
#
# while queue:
#     swap = queue.popleft()
#     print(queue)
#     if cnt == K:
#         out += 1
#         cnt = 1
#         if swap == M:
#             break
#     else:
#         queue.append(swap)
#         cnt += 1
#
# print(out)

# queue 쓰면 메모리 터지니까 규칙찾아서 계산하기

# 5  2  3
# N  K  M
# 1 2 3 4 5

# tmp 계산
# first_out = ((K%N) + (out * K))%N = ((2%) + (0 * 2))%5 = 2
# second_out = (K%N) + (out * K))%N = ((2%5) + (1 * 2))%5 = 4
# 한바퀴 돌았을 경우 (tmp 결과가 한바퀴 돌게 된다면 +1하기), 전체 길이를 K로 나눴던 몫만큼 빼야 함
# third_out = (K%N) + (out * K))%N = ((2%5) + (3 * 2))%5 + 1
N, K, M = map(int, input().split())
cnt = 1
out = 0

while out < N:
    # 한명 나갔으면 그 다음 내보낼 때는 한명이 줄어듬(out += 1)
    out += 1
    # 즉, 나갈 순서를 체크하는 tmp는 cnt를 N-out + 1로 나눈 나머지여야 함
    # tmp가 M과 같아진다면 break
