# # 시간 제한이 뜬다
# import sys
# n = int(sys.stdin.readline())
# a = list(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# b = list(map(int,sys.stdin.readline().split()))
# for i in b:
#     if i in a:
#         print(1)
#     else:
#         print(0)
#
# # 정렬을 해보자
# import sys
# n = int(sys.stdin.readline())
# a = sorted(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# b = sorted(map(int,sys.stdin.readline().split()))
# for i in b:
#     if i in a:
#         print(1)
#     else:
#         print(0)
        
# b는 정렬하면 안되지 멍청아...
# a는 그냥 set으로 해도 되는거 아닌가? 비교만 하면 되니까
# 런타임 에러
# import sys
# n = int(sys.stdin.readline())
# a = set(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# b = list(map(int,sys.stdin.readline().split()))
# for i in b:
#     if a.count(i)>=1:
#         print(1)
#     else:
#         print(0)

# 걍 in으로
# 드디어 맞네. count보다 in이 효율적인 듯 하다.
import sys
n = int(sys.stdin.readline())
a = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
for i in b:
    if i in a:
        print(1)
    else:
        print(0)

# 이진 탐색으로도 풀어 보자.