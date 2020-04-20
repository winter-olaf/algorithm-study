# strike와 ball을 비교하는 함수 선언
def check_sb(examples,cases):
    strikes, balls = (0,0)
    for i in range(3):
        if examples[i] == cases[i]:
            strikes += 1
        elif examples[i] in cases:
            balls += 1
    return (strikes,balls)

# 한가지 기능만 import할 때 from을 사용하면 사용할 때에 덜 귀찮음
from itertools import permutations
def solution(baseball):
    ables = []
    # str 형식의 list로 1~9까지의 모든 경우의 수 리스트인 cases 생성
    cases = list(''.join(x) for x in permutations([str(i) for i in range(1,10)],3))
    # 주어진 예시 baseball의 원소마다
    for numbers,strikes,balls in baseball:
        # 모든 case를 비교하면서 같은 strikes와 balls를 가진 경우를 가져옴
        ables = [case for case in cases if check_sb(str(numbers),case) == (strikes,balls)]
    return ables


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	))
