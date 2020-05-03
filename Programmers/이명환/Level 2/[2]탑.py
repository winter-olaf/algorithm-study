def solution(heights):
    answer = [0 for i in range(len(heights))]
    for i in range(-1,-len(heights),-1):
        for k in range(i-1,-len(heights)-1,-1):
            if heights[k]> heights[i]:
                answer[i] = k+len(heights)+1
                break
    return answer