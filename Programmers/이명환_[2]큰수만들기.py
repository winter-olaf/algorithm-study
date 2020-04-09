# 앞에서부터 숫자를 세어나감, 가장큰 수를 찾고
# 그 앞쪽의 숫자를 작은 순서대로 지워 나감.
# import operator
# def solution(num, k):
#     ans = []
#     num_list = list(map(int, num))
#     x = sorted(enumerate(num_list), key=operator.itemgetter(1),reverse = True)
#     for i in x:
#         if i[0] - k <= 0:
#             idx,value = i
#             ans.append(value)
#             for i in range(idx + 1):
#                 del num_list[0]
#             k -= idx
#             break
#
#     while(k!=0):
#         del num_list[0]
#         if num_list == []:
#             break
#         idx,value = max(enumerate(num_list), key=operator.itemgetter(1))
#         for i in range(idx+1):
#             if idx == 0:
#                 break
#             num_list.remove(min(num_list[:idx]))
#             k-=1
#             if k==0:
#                 for k in num_list:
#                     ans.append(k)
#                 break
#         ans.append(value)
#
#     return ans

# def solution(number, k):
#     num_list = list(map(int, number))
#     answer = ''
#     ans = [num_list.pop(0)]
#     while(k != 0):
#         if ans[-1] < num_list[0]:
#             if max(ans) < num_list[0] and len(ans) <= k:
#                 k -= len(ans)
#                 ans = [num_list.pop(0)]
#                 continue
#             ans.pop(-1)
#             ans.append(num_list.pop(0))
#             k -=1
#         else :#ans[-1]>= num_list[0]
#             ans.append(num_list.pop(0))
#
#     for i in num_list:
#         ans.append(i)
#     for i in ans:
#         answer += str(i)
# 
#     return answer
def solution(number, k):
    # 1. 스택 생성
    st = []

    # 2. 큰 수가 앞자리가 되게끔 스택에 저장합니다.
    for elem in number:
        while st and st[-1] < elem and k > 0:
            st.pop()
            k -= 1

        st.append(elem)

    # 3. k가 남았다면 뒤에서부터 뺍니다.
    while k > 0:
        st.pop()
        k-=1

    answer = "".join(st)
    return answer


print(solution("4177252841",4))









