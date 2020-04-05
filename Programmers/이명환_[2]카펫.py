def solution(br, re):
    exter = (br- 4)/2
    # 빨간 블록에 맞닿은 브라운 블럭의 가로 세로 합
    for x in range(br):
        for y in range(br):
            if x+y == exter and x*y ==re and x>=y:
                #빨간 블록에 맞닿은 브라운 블럭의 가로 세로 합을 만족하고
                #빨간 격자에 맞닿은 브라운 블럭의 가로 * 세로 = red를 만족하고
                #가로가 세로보다 긴 x,y를 구함
                answer = [x+2,y+2]
                #빼놓았던 격자 4개를 각각 가로세로에 더함
                break
    return answer