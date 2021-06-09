def bit_cal(num):
    res = num + 1
    a = bin(num)[::-1][:-2]
    while 1:
        b = bin(res)[::-1][:-2]
        l = len(b)
        cnt = 0
        for i in range(l):
            if cnt > 2:
                break
            try:
                if a[i] != b[i]:
                    cnt += 1
            except IndexError:
                cnt += 1

        if cnt <= 2:
            return res

        res += 1

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(bit_cal(number))
    return answer

print(solution([2,7]))