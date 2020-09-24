# Greedy

# 정답은 통과됐지만 이상한 문제
n, k = map(int, input().split())
num = list(input())
result = []
# 앞에 나온 숫자가 뒤에 나온 숫자보다 작을 경우 쳐낸다는 마인드
for i in range(n):
    while k > 0 and result:
        if result[-1] < num[i]:
            result.pop()
            k -= 1
        else:
            break
    result.append(num[i])
# k가 0 이상인데 남은 수가 같은 수일 경우를 생각해 줘야 한다
print(''.join(result[:n-k]))
# 아래의 코드라고 생각했는데, 이렇게 하면 k가 0이 될 경우 [:0]을 출력해 버린다.
# print(''.join(result[:-k]))

'''
n, k = map(int,input().split())
num = list(input())
result, dk = [], k
# 앞에 나온 숫자가 뒤에 나온 숫자보다 작을 경우 쳐낸다는 마인드
for i in range(n):
    while dk>0 and result:
        if result[-1] < num[i]:
            result.pop()
            dk-=1
        else:
            break
    result.append(num[i])
# k가 0 이상인데 남은 수가 같은 수일 경우를 생각해 줘야 한다
print(''.join(result[:n-k]))
'''


'''
4 2
1924

4 2
1324

잘못된 위 풀이의 반례
7 5
9929191

5 3
99291

6 3
773671

'''
