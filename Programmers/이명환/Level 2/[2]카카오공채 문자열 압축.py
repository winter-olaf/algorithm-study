# def solution(s):
#     slice = 1
#     min_len = len(s)
#     ans_list = []
#     while(slice < len(s)//2+1):
#         cnt = 0
#         s_copy = s
#         ans = ''
#         while(True):
#             x = int(cut(s_copy,slice))
#             y = str(x)
#             if y != '1':
#                 ans += y + s_copy[:slice]
#             else:
#                 y= ''
#                 ans += y + s_copy[:slice]
#             s_copy = s_copy[x*slice:]
#           # 다음에 잘라야하는 단어의 길이가 s_copy의 길이보다 클 때 break
#             if 2*slice+1 > len(s_copy):
#                 break
#         slice +=1
#         k = "".join(ans)
#         str_len = len(k)
#         if str_len < min_len and str_len != 0:
#             min_len = str_len
#     return min_len
#
# def cut(s,slice):
#     n= 1
#     while(True):
#         if s[:slice] == s[n*slice:(n+1)*slice]:
#             n += 1
#             if (n+1) *slice > len(s):
#                 return n
#         else:
#             return n
#
# print(solution(	"abcabcdede"))
# 정확성: 8.0
# 합계: 8.0 / 100.0

def solution(s):
   len_s = len(s)
   ans= len_s
   for i in range(1, (len_s//2)+1):
       bef=s[:i]
       slice=i
       same=1
       temp=len_s
       while (True):
           #다음 자를 단어가 s의 길이보다 클 때 break
           if slice+i > len_s:
               break
            #판별하는 단어 뭉치가 같을 때
           if bef == s[slice:slice+i]:
               same+=1
               #자른만큼 문자열의 길이를 빼줌
               temp-=i
           else:
               #same이 10일 경우를 생각해서 str 후 len을 구해줌
               if same>1:
                   temp+=len(str(same))
               same=1
               bef=s[slice:slice+i]
           slice +=i
       if same>1:
           temp+=len(str(same))
       ans = min(ans, temp)
   return ans
