def cal(ls, rs, dest, hand):
    global cl, cr

    if dest in [1,4,7]:
        pass
    elif dest in [3,6,9]:
        pass


cl, cr = -1, -2

def solution(numbers, hand):
    answer = ''

    for number in numbers:
        answer += cal(cl, cr, number, hand)
    return answer
