# 문제를 제대로 읽지 않고 풀어서 '가장 큰 수'를 찾아버림

# import itertools

# def solution(num,k):

#     arr = []
#     res = []

#     for i in num:
#         arr.append(i)
#     # 오; 문자열도 숫자가 큰게 정렬이 된다는걸 알았음
#     arr.sort(reverse=True)

#     for i in range(k):
#         arr.pop()
    
#     res = max(list(map(''.join, itertools.permutations(arr))))
#     return res

# 앞에서 수를 정하는 동작이 뒤에서의 선택에 의해 바뀔 필요가 없으므로 이 문제에서 최적해를 찾기 좋은 탐욕법을 사용하기로 함

# 91.7/100 이 나와서 뭐가 문제인가 생각해보니 이미 내림차순으로 정리되어 있는 수의 경우를 고려해줘야 했다 (#1 부분)
def solution(num,k):   
    # Stack
    res = []

    for idx,val in enumerate(num):
        while res and res[-1] < val and k > 0:
            res.pop()
            k -= 1
        
        # k가 0이 되면 이후의 숫자를 주르륵 더한다
        if k == 0:
            res += num[idx:]
            break
        # 조건이 없을 경우 결과 리스트에 추가
        res.append(val)
    #1 이 부분을 추가했다. k값만큼 뒤를 자름
    res = res[:-k] if k>0 else res
    
    # #2 #1을 지우고 이렇게만 써도 됨.
    # if k>0:
    #     res = res[:-k]
    
    # #3 else를 빼도 된다고 생각했는데 빼니까 런타임 에러가 뜸. Hmm..
    # res = res[:-k] if k>0

    ans = ''.join(res)
    return ans
print(solution('54321',2))