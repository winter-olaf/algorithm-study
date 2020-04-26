def solution(skill, skill_trees):
    answer = 0
    li_sk = list(skill)

    for i in skill_trees:
        idx_tr = []
        li_tr = list(i)
        for k in li_tr:
            for idx,j in enumerate(li_sk):
                if j == k:
                    idx_tr.append(idx)
        if idx_tr == []:
            answer+=1
        else:
            a = len(idx_tr)
            b = [i for i in range(a)]
            if idx_tr == b:
                answer += 1
    return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])

# while(True):
#
#     if idx_tr ==[]:
#         answer+=1
#         break
#     temp = min(idx_tr)
#     if idx_tr[0]== temp:
#         idx_tr.pop(0)
#     else:
#         break