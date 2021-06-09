def bit_cal(num):
    res = num + 1
    a = bin(num)[::-1][:-2]
    l = len(a)
    while 1:
        b = bin(res)[::-1][:-2]
        cnt = 0
        for i in range(l):
            if cnt > 2:
                break
            if a[i] != b[i]:
                cnt += 1

        # 더 큰 수일 경우 1이 나오는 만큼 cnt 추가
        for i in range(len(b)-l):
            if cnt > 2:
                break
            if b[i+len(b)-1] == '1':
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