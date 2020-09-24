# Greedy
n, k = map(int,input().split())
num = list(input())
result = []
# 앞에 나온 숫자가 뒤에 나온 숫자보다 작을 경우 쳐낸다는 마인드
for i in range(n):
    while k>0 and result:
        if result[-1] < num[i]:
            result.pop()
            k-=1
        else:
            break
    result.append(num[i])
# k가 0 이상인데 남은 수가 같은 수일 경우를 생각해 줘야 한다
print(''.join(result[:n-k]))

'''
4 2
1924

4 2
9999
'''
