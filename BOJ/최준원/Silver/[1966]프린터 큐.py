# 틀렸습니다~♬

# from sys import stdin,stdout
# T = int(input())
# result=""
# for i in range(T):
#     n,m = map(int,stdin.readline().split())
#     p = list(map(int,stdin.readline().split()))
#     base = sorted(p,reverse=True).index(p[m]) # 정렬했을 때 가장 첫번째로 나오는 해당 값
#     maxP = max(p)
#     # 원소가 하나인 경우
#     if n == 1:
#         result+='1'
#         continue
#     # 정렬되기 전 최대값보다 앞에 있는 경우
#     elif m < p.index(maxP):
#         for i in p[m+1:p.index(maxP)]:
#             if p[m] < i:
#                 base+=1
#         for i in p[p.index(maxP):]:
#             if p[m] == i:
#                 base+=1
#     # 정렬되기 전 최대값보다 뒤에 있는 경우
#     else:
#         for i in p[p.index(maxP):m]:
#             base+=1
#     result+=str(base+1)
# stdout.write('\n'.join(result))

# 정렬이 필요 없나?
# 또 틀렸군..ㅋㅋ
# from sys import stdin,stdout
# T = int(input())
# result=""
# for i in range(T):
#     n,m = map(int,stdin.readline().split())
#     p = list(map(int,stdin.readline().split()))
#     prior = p.index(max(p))
#     base = 0
#     if n == 1:
#         result+='1'
#         continue
#     if m < prior:
#         for i in p[:m]:
#             if p[m]<=i: base+=1
#         for i in p[m+1:prior]:
#             if p[m]<i: base+=1 
#         for i in p[prior:]:
#             if p[m]<=i: base+=1
#     else:
#         for i in p[prior:m]:
#             if p[m]<=i: base+=1
#     result+=str(base+1) # 인덱스 값이니 1 더하기
# stdout.write('\n'.join(result))

# 데큐를 써보자 써보자~
# 오! 임의의 배열을 한개 더 쓰면 편하구나!
from sys import stdin,stdout
from collections import deque
T = int(input())
for i in range(T):
    n,m = map(int,stdin.readline().split())
    p = list(map(int,stdin.readline().split()))
    tmp = deque([0 for x in range(n)])
    tmp[m] = 'C' # 임시 배열에 변수 넣기

    que = deque(p)
    cnt = 0
    while True:
        # 만약 큐의 첫번째가 큐의 최대값이면
        if que[0] == max(que):
            cnt+=1
            if tmp[0] == 'C': # 만약 원하는 수가 뽑힌다면 break하고 지금까지 쌓인 count 출력
                print(cnt)
                break
            else:
                que.popleft()
                tmp.popleft()
        # 최대값이 아니면 가차없이 뒤로 보낸다
        else:
            que.append(que.popleft())
            tmp.append(tmp.popleft())