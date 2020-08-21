# import sys
#
# N = int(sys.stdin.readline())
# stairs = [0]
# for i in range(N):
#     stairs.append(int(sys.stdin.readline()))
# score = [0]*(N+1)
#
# def stepUp(idx,stack):
#     if idx == N:
#         return
#     if idx+2 <= N and score[idx+2] <= stairs[idx+2] + score[idx]:
#         score[idx+2] = stairs[idx+2] + score[idx]
#         stepUp(idx+2,1)
#     if score[idx+1] <= stairs[idx+1] + score[idx] and stack != 2:
#         score[idx+1] = stairs[idx+1] + score[idx]
#         stepUp(idx+1,stack+1)
#
# stepUp(0,0)
# print(score[-1])
# 왜안되지ㄹㅇ

# import sys
#
# N = int(sys.stdin.readline())
# stairs = [0]
# for i in range(N):
#     stairs.append(int(sys.stdin.readline()))
# score = [0]*(N+1)
# answer = []
#
# def stepUp(idx,stack):
#     if idx == N:
#         answer.append(score[idx])
#         return
#     if idx+2 <= N :
#         score[idx+2] = stairs[idx+2] + score[idx]
#         stepUp(idx+2,1)
#     if score[idx+1] <= stairs[idx+1] + score[idx] and stack != 2:
#         score[idx+1] = stairs[idx+1] + score[idx]
#         stepUp(idx+1,stack+1)
#
# stepUp(0,0)
# print(max(answer))
#시간초과

import sys

N = int(sys.stdin.readline())
stairs = list()
for i in range(N):
    stairs.append(int(sys.stdin.readline()))
if N ==1:
    print(stairs[0])
elif N == 2:
    print(sum(stairs))
else:
    score = list()
    score.append(stairs[0])
    score.append(stairs[1] + stairs[0])
    score.append(max(stairs[1] + stairs[2], stairs[0] + stairs[2]))

    for i in range(3, N):
        score.append(max(stairs[i] + score[i - 2], stairs[i] + stairs[i - 1] + score[i - 3]))
    print(score[N - 1])
    #다이나믹 프로그래밍 어렵네 ;; DFS로 풀려다가 피봤다.
