# 메모리 초과
# from sys import stdin
# n = int(stdin.readline())
# arr = [int(stdin.readline()) for x in range(n)]
# for i in sorted(arr):
#     print(i)

# 수를 10,000,000까지, 10000개보다 작거나 같은 수까지 받는다.
# for문으로 수를 받는 부분의 배열을 미리 생성해 보자
# 또 메모리 초과
# from sys import stdin
# n = int(stdin.readline())
# arr = [0]*10000
# arr = [int(stdin.readline()) for x in range(n)]
# for i in sorted(arr):
#     print(i)

# 입력받은 모든 값을 저장하면 안된다는 결론.
# 미리 결과값 리스트를 만든다
# 성공! 그런데 9336ms 걸리는게 맞는건가? 다른 사람들 것 보니까 비슷한듯. 역시 파이썬은 속도가 쫌....
from sys import stdin
n = int(stdin.readline())

arr = [0]*10000

for i in range(n):
    # 입력받은 값이 3이면 음... 딱 떨어지게 1만 배열 만들고 싶으니 인덱스를 하나 줄이는 걸로(3 입력받으면 2 인덱스 1 추가)
    arr[int(stdin.readline())-1]+=1

for i in range(len(arr)):
    # 1부터 시작했을 때, 입력받은 값의 수만큼 해당 숫자 출력하기
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)

