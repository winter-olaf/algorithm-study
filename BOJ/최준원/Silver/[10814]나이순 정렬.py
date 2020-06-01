# 이게 왜 안맞는거지..? 흠.
import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a,b = map(str,sys.stdin.readline().split())
    arr.append((a,b))
for a,b in sorted(arr, key=lambda i:i[0]):
    print(a,b)

# lambda 키를 바꿔봄
import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a,b = map(str,sys.stdin.readline().split())
    arr.append((a,b))
    # 문자형으로 된 숫자도 어차피 정렬하면 정렬이 되기 때문에 괜찮다고 생각했지만, 그 부분이 문제였나 봄...
for a,b in sorted(arr, key=lambda i:int(i[0])):
    print(a,b)