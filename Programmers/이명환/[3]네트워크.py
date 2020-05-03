#computers[i][j] (i = 0),(j = 1) 부터 순차적으로 탐색한다.
#computers[i][j]가 0이 아닐 때 n-=1,i+=1,j+=1 하고 computers를 다시 탐색한다.
#0인 경우 그냥 j+=1 해준다.
# def solution(n, computers):
#     answer = n
#     i,j = 0,1
#     while(True):
#         if computers[i][j] != 0 :
#             answer -= 1 + network_check(n,i,j,computers)
#         j+=1
#         if j == n:
#             break
#     return answer
#
# def network_check(n,i,j,computers):
#     i=j
#     j+=1
#     temp = 0
#     while(True):
#         if j == n:
#             return temp
#         if computers[i][j] != 0:
#             temp = 1 + network_check(n,i,j,computers)
#             return temp
#         else:
#             j+=1

# 기본테스트 케이스는 통과하는데 실행하면 다틀림
# 아마 동떨어진 네트워크 ex) [[1,0,0,1][0,1,1,0][0,1,1,0][1,0,0,1]]이런게 계산이 안되는 듯

def solution(n, computers):
    answer = n
    i,j = 0,1
    while(True):
        if j== n:
            i+=1
            if i == n:
                return answer
            if computers[i][i] == 0:
                while(computers[i][i]!=1):
                    i+=1
                    if i ==n:
                        return answer
            j = i+1
        if i == n or j >=n :
            return answer
        if computers[i][j] != 0 :
            answer -= 1 + network_check(n,i,j,computers)
        j+=1

def network_check(n,i,j,computers):
    i=j
    computers[i][i] = 0
    temp = 0
    j+=1
    while(True):
        if j == n:
            return temp
        if computers[i][j] != 0:
            temp += 1 + network_check(n,i,j,computers)
        else:
            j+=1
# 정확성: 23.1
# 합계: 23.1 / 100.0
# 거의 다 시간초과로 실패함. while 문을 못빠져나오는 걸까..