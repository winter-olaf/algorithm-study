# 0층의 i호에는 i명이 산다는 것을 중점으로 생각하면 쉬운 문제.
# 0층의 1호에는 1명, 2호에는 2명...
for _ in range(int(input())):
    k=int(input());n=int(input())
    ho=[i for i in range(1,n+1)] # 아파트 호수 1,2,3,4...호
    for i in range(k): # 층의 높이만큼 반복
        for j in range(1,n): # 호수-1만큼 반복. 만약 3층 3호라면, 3층 2호 + 2층 3호다.
            ho[j]+=ho[j-1] # 호수에 이전의 호의 값을 더한다. 
        print(ho[n-1])
