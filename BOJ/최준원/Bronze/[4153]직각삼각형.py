# 생각을 하고 문제를 풀자
# 정렬을 하지 않으면 가장 긴 것을 빗변으로 받을 수가 없다
while True:
    # 애초에 정렬해서 받기
    a = sorted(list(map(int,input().split())))
    if sum(a)==0:
        break
    # 리스트 두개를 붙여서 뒤의 리스트를 조건문으로 사용하는 방식
    # 조건에 맞으면 1번째 인덱스, 아니면 0번째 인덱스를 출력
    print(['wrong','right'][a[0]**2 + a[1]**2 == a[2]**2])
    
# 다른 사람의 풀이
# 궁극의 숏코딩은 True를 1로 쓰는 것...
while 1:
 a,b,c=sorted(map(int,input().split()))
 if a==0:break
 print("wrriognhgt"[a*a+b*b==c*c::2])