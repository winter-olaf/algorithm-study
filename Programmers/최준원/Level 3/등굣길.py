def solution(m, n, puddles):
    data = [[0] * (m+1) for _ in range(n+1)]
    data[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==j==1:
                continue
            if [j,i] in puddles:
                continue
            data[i][j] = data[i-1][j] + data[i][j-1]

    return data[n][m]%1000000007

print(solution(4, 3, [[2, 2]]))