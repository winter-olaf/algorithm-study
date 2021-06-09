def bit_cal(num):
    res = num + 1
    a = bin(num)[2:][::-1]
    while 1:
        tmp = bin(num & res)[2:][::-1]
        b = bin(res)[2:][::-1]
        cnt = 0
        for i in range(len(tmp)):
            if cnt > 2:
                break
            if tmp[i] != a[i]:
                cnt += 1
        cnt += len(b) - len(tmp)
        if cnt <= 2:
            return res

        res += 1

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(bit_cal(number))
    return answer

print(solution([2, 7]))