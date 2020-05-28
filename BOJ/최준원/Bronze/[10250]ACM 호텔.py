t = int(input())

# 최종 결과를 저장하는 리스트
result = []

# 호텔 객실을 리스트 형태로 만들어 n번째 손님을 인덱싱
def acm(h,w,n):
    acm = []
    for i in range(1,w+1):
        for j in range(1,h+1):
            acm.append(j*100+i)
    result.append(acm[n-1])

# 입력을 받고 acm 함수를 사용해 바로 result에 결과 추가
for x in range(t):
    h,w,n = map(int, input().split())
    acm(h,w,n)

for i in result:
    print(i)

# 다른 코드
# 근데 이게 왜 맞는지 모르겠다...? 한번에 출력해 내야 하는거 아닌가? 이렇게 하면 입력할때마다 원라인씩 출력되는데
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    print(((n-1)//h)+1+((n-1) % h+1)*100)
