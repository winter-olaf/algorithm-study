# strike와 ball을 비교하는 함수 선언
def check_sb(examples,cases):
    strikes, balls = (0,0)
    for i in range(3):
        if examples[i] == cases[i]:
            strikes += 1
        elif examples[i] in cases:
            balls += 1
    return (strikes,balls)

# def check_sb(examples,cases,s,b):
#     strikes, balls = (0,0)
#     for i in range(3):
#         if examples[i] == cases[i]:
#             strikes += 1
#         elif examples[i] in cases:
#             balls += 1
#     if s != strikes:
#         return False
#     if b != balls:
#         return False
#     return True

# 한가지 기능만 import할 때 from을 사용하면 사용할 때에 덜 귀찮음
from itertools import permutations
def solution(baseball):
    able = []
    # str 형식의 list로 1~9까지의 모든 경우의 수 리스트인 cases 생성
    cases = list(''.join(x) for x in permutations([str(i) for i in range(1,10)],3))
    '''
    # 주어진 예시 baseball의 원소마다
    for numbers,strikes,balls in baseball:
    # 모든 case를 비교하면서 같은 strikes와 balls를 가진 경우를 가져오려 했음 그런데 이렇게 하니깐 각 case를 모든 numbers와 비교하질 못함...
        ables = [case for case in cases[:] if check_sb(str(numbers),case) == (strikes,balls)]
    return ables
    '''
    # 그래서 아닌 경우를 싹 삭제해 보기로 함
    for numbers,strikes,balls in baseball:
        # 그래도 안되다가 cases가 아닌 cases[:]를 쓰니 됨. 무슨 차이인지..
        for case in cases[:]:
            if check_sb(str(numbers),case) != (strikes,balls):
                cases.remove(case)
    return len(cases)



print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	))
