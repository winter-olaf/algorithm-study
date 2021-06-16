from collections import deque

def solution(places):
    answer = []

    # BFS, 거리가 2 미만일 때까지만 탐색
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for place in places:
        arr = [list(x) for x in place]

        flag = True

        for i in range(5):
            for j in range(5):
                # 효율성
                if not flag:
                    break

                if arr[i][j] == 'P':
                    # BFS
                    Q = deque([(i,j,0)])

                    visited = [[0]*5 for x in range(5)]
                    visited[i][j] = 1
                    while Q:
                        cr, cc, cd = Q.popleft()
                        for dr, dc in delta:
                            nr = cr + dr
                            nc = cc + dc
                            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and cd < 2 and arr[nr][nc] != 'X':
                                if arr[nr][nc] == 'P':
                                    # 거리두기 실패!
                                    flag = False
                                    break
                                Q.append((nr,nc,cd+1))
                                visited[nr][nc] = 1
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))