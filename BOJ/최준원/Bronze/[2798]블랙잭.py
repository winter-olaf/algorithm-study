# permutation을 이용한 풀이
# 가능한 모든 조합 중 m보다 작은 수를 결과 리스트에 저장한 뒤, 내림차순 정렬한 뒤 0번째 인덱스를 출력한다
# '가능한 모든 조합'을 이용하기에 오래 걸릴 수도 있겠다고 생각함
# max 함수를 써도 되긴 하겠다
import itertools
n,m = map(int,input().split())
card = list(map(int,input().split()))
tmp = list((itertools.permutations(card,3)))
result = []
for i in tmp:
    if sum(i) <= m:
        result.append(sum(i))
print(sorted(result,reverse=True)[0])

# 다른 사람의 풀이
N, M = map(int, input().split())
ss = list(map(int, input().split()))

noms = []

for i in range(len(ss)):
    for j in range(i+1, len(ss)):
        for k in range(j+1, len(ss)):
            if ss[i] + ss[j] + ss[k] <= M:
                noms.append(ss[i] + ss[j] + ss[k])

print(max(noms))
