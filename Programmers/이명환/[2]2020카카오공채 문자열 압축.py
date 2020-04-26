# def solution(s):
#     slice = 1
#     ans_list = []
#     while(slice != len(s)/2+1):
#         cnt = 0
#         s_copy = s
#         ans = ''
#         while(True):
#             x = cut(s_copy,slice)
#             print(x)
#             y = str(x)
#             ans += y + s_copy[:slice]
#             s_copy = s_copy[slice*x:]
#             if (x+1) *slice > len(s):
#                 break
#         slice +=1
#         ans_list += ans
#     return min(ans_list)
#
# def cut(s,slice):
#     n= 1
#     while(True):
#         if s[:slice] == s[n*slice:(n+1)*slice]:
#             n += 1
#             if (n+1) *slice > len(s):
#                 return n
#         else:
#             if n == 1:
#                 return ''
#             else:
#                 return n
#
# solution("ababcdcd")
# TypeError: slice indices must be integers or None or have an __index__ method