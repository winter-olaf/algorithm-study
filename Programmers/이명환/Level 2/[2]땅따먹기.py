# def solution(land):
#     # cur_idx 현재 행
#     temp1 =max(land[0])
#     cur_idx = land[0].index(max(land[0]))
#     for i in land[1:]:
#         if cur_idx != i.index(max(i)):
#             cur_idx = i.index(max(i))
#             temp1 += max(i)
#         else:
#             a = sorted(i,reverse=True)
#             cur_idx = i.index(a[1])
#             temp1 += a[1]
#
#     b = sorted(land[0],reverse=True)
#     temp2 = b[1]
#     cur_idx = land[0].index(b[1])
#     for i in land[1:]:
#         if cur_idx != i.index(max(i)):
#             cur_idx = i.index(max(i))
#             temp2 += max(i)
#         else:
#             a = sorted(i,reverse=True)
#             cur_idx = i.index(a[1])
#             temp2 += a[1]
#     ans = max(temp1,temp2)
#     return ans
# 테스트 케이스 통과 but 제출하기 다틀림

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    print(land[len(land)-1])
    return max(land[len(land) - 1])

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])