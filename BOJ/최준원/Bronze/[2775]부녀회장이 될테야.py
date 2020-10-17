# 1 2   3   4   5   6
# 1 3   6   10  15  21
# 1 4   10  20  35  56 
# 수열의 점화식은 d[i][j] = d[i-1][j] + d[i][j-1]
# 0층의 i호에는 i명이 산다는 것을 중점으로 생각하면 쉬운 문제.
# 0층의 1호에는 1명, 2호에는 2명...
for _ in range(int(input())):
    k=int(input());n=int(input())
    ho=[i for i in range(1,n+1)] # 아파트 호수 1,2,3,4...호
    for i in range(k): # 층의 높이만큼 반복
        for j in range(1,n): # 각 층의 1호(Index 0)는 생각할 필요가 없으므로 생략한다. n-1호까지 계산.
            ho[j]+=ho[j-1] # 호수에 이전의 호의 값을 더한다. 
        print(ho[n-1]) # 인덱스로 계산해야 하니 n-1의 값을 출력