# N = int(input())
# # 666 1666 2666 3666 4666 5666 6661 6662 6663 6664 6665 6666 6667 6668 6669
# cnt = 0
# start = 666
# res = 0
# while cnt < N:
#     tmp = start
#     while tmp:
#         if tmp%10 == 6 and tmp//10%10 == 6 and tmp//10//10%10 == 6:
#             cnt += 1
#             res = start
#             break
#         else:
#             tmp //= 10
#     start += 1
#
# print(res)

N = int(input())
cnt = 0
start = 666

while 1:
    if '666' in str(start):
        cnt += 1
        if cnt == N:
            print(start)
            break
    start += 1

