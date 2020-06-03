# 시간 초과
# import sys
# a,b,v = map(int,sys.stdin.readline().split())
# i = 0
# day = 0
# while 1:
#     i+=a
#     day+=1
#     if i>=v:
#         print(day)
#         break
#     i-=b

# # 너무 대충푼듯.. 틀림
# import sys
# a,b,v = map(int,sys.stdin.readline().split())
# sub = v-a+b
# x = a-b
# i=1
# while 1:
#    x*=i
#    i += 1
#    if x>=sub:
#        print(i)
#        break

# 아 이게 왜틀리지?
# import sys
# a,b,v=map(int,sys.stdin.readline().split())
# print((v-a)//(a-b)+1)


# 제발
import sys
a,b,v = map(int, sys.stdin.readline().split())
h = v-b # 올라야 하는 최종 높이(마지막날 안떨어짐)
r = a-b # 하루에 올라가는 높이
if h%r==0:
    print(h//r)
else:
    print(h//r+1)