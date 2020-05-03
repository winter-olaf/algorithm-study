# why i have to use stack...?
def solution(heights):
    result = [0]*len(heights)
    for i in range(len(heights)-1,0,-1):
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                result[i] += j+1
                break
    return result

print(solution([6, 9, 5, 7, 4]))
