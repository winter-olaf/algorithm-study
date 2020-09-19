# 시각
# 3중 for문을 써도 경우의 수가 24 X 60 X 60  = 86,400이기에 풀이가 가능하다.
n = int(input())
result = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                result+=1
print(result)