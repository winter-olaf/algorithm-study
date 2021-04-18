from pprint import pprint
def solution(r, c, board):
    answer = 0
    data = [['']*r for x in range(c)]

    for i in range(c):
        for j in range(r-1, -1, -1):
            data[i][r-j-1] = board[j][i]

    while True:
        flag = False
        visited = [[0]*r for x in range(c)]
        # 종료조건 - -2, -2 인덱스에 도착했는데 지울 칸이 없는 경우
        for i in range(c-1):
            for j in range(r-1):
                # ''가 아닌지 체크를 안했다;;
                if data[i][j] != '' and data[i][j] == data[i+1][j] == data[i][j+1] == data[i+1][j+1]:
                    flag = True
                    visited[i][j] = 1
                    visited[i+1][j] = 1
                    visited[i][j+1] = 1
                    visited[i+1][j+1] = 1

        if not flag:
            break

        for i in range(c):
            for j in range(r):
                if visited[i][j]:
                    answer += 1
                    data[i][j] = ''

        # 다 지운다음에 앞으로 땡기기
        for i in range(c):
            tmp = []
            for j in range(r):
                if data[i][j] != '':
                    tmp.append(data[i][j])

            for x in range(r-len(tmp)):
                tmp.append('')


            data[i] = tmp

    return answer

print(solution(4, 5 ,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6 ,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))