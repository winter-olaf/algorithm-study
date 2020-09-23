# 그리디 알고리즘
n = int(input())
negative, positive = [], []
zero = 0
result = 0

for _ in range(n):
    m  = int(input())
    if m < 0:
        negative.append(m)
    elif m == 0:
        zero+=1
    else:
        positive.append(m)

negative.sort()
positive.sort(reverse=True)
# 음수
for i in range(0, len(negative)-1 ,2):
    result += (negative[i]*negative[i+1])
# 음수의 개수가 홀수개이고 0을 못받았을 경우
if len(negative)%2 == 1 and zero == 0:
    result += negative[-1]
# 양수
for i in range(0, len(positive)-1, 2):
    if positive[i] != 1 and positive[i+1] != 1:
        result += (positive[i]*positive[i+1])
    else:
        result += (positive[i]+positive[i+1])
if len(positive)%2 == 1:
    result+=positive[-1]
print(result)