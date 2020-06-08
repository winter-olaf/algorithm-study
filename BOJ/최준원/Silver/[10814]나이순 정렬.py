# 이게 왜 안맞는거지..? 흠.
import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a,b = map(str,sys.stdin.readline().split())
    arr.append((a,b))
for a,b in sorted(arr, key=lambda i:i[0]):
    print(a,b)
#     # sait2000의 답변: 문자열로 된 숫자는 "10"<"9" 와 같은 경우가 있기 때문에 int형으로 바꾼 key를 사용해야 한다. 둘다 자릿수가 같으면 정상적으로 비교가 되지만, 100 <99 / 3000 <333 등 자릿수가 바뀌면 비교가 안된다.
# 2
# 10 John
# 9 John
# 10 John
# 9 John

# # lambda 키를 바꿔봄
# import sys
# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     a,b = map(str,sys.stdin.readline().split())
#     arr.append((a,b))
#     # 문자형으로 된 숫자도 어차피 정렬하면 정렬이 되기 때문에 괜찮다고 생각했지만, 그 부분이 문제였나 봄...

# for a,b in sorted(arr, key=lambda i:int(i[0])):
#     print(a,b)