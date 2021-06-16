def cal(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    # 이미 뽑은 로또 수가 당첨에 몇 개 있는지 카운트하고 0의 갯수를 카운트
    zero = 0
    dup = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        elif lotto in win_nums:
            dup += 1

    min_val = cal(dup)
    max_val = cal(dup + zero)
    return [max_val, min_val]
