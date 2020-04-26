# dynamic programming이 필요함. Greedy는 안되는 이유 = Greedy가 최적의 값이 아닐 수도 있기 때문에!
import copy
def solution(land):
    for i in range(1,len(land)):
        land[i][0] = max(land[i-1][1:]) + land[i][0]
        land[i][1] = max(land[i-1][0], land[i-1][2],
                         land[i-1][3]) + land[i][1]
        land[i][2] = max(land[i-1][0],land[i-1][1],land[i-1][3]) + land[i][2]
        land[i][3] = max(land[i-1][0],land[i-1][1],land[i-1][2]) + land[i][3]
    return max(land[-1])

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]	))

# copy를 이용한 다른 사람의 풀이
def hopscotch(board, size):
    result = 0
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    for i in range(1, size):
        for j in range(4):
            temp = copy.deepcopy(board[i-1])
            temp[j] = 0
            board[i][j] += max(temp)
    result = max(board[-1])
    return result
