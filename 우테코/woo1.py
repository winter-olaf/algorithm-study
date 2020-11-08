def solution(grades, weights, threshold):
    score = {"A+":10, "A0":9,"B+":8,"B0":7,"C+":6,"C0":5,"D+":4,"D0":3,"F":0}
    result = 0
    for g in range(len(grades)):
        result+= score.get(grades[g]) * weights[g]
    return (result - threshold)