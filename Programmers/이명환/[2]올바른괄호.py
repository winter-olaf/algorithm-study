# def solution(s):
#     while (True):
#         if s.find('()') != -1:
#             s = s.replace('()', "")
#         else:
#             break
#     if s != '':
#         return False
#     return True
#
# print(solution('(())()'))
# 효율성 테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)

def solution(s):
    count=0
    for i in s:
        if i=='(':
            count+=1
        else:
            if count==0: return False
            else:count-=1
    if count==0:return True
    else : return False