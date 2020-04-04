#받은 문자열을 리스트로 만들어서 리스트의 원소들을 조합
#그 조합이 소수가 맞는지 아닌지 확인
import itertools
def solution(numbers):
    answer = 0
    a = []
    num = list(numbers)
    #['0','1','1']
    for x in range(len(num)):
        a += list(map(int,list(map(''.join, itertools.permutations(num,x+1)))))
    #가능한 조합 모두 a 리스트에 넣기
    a = set(a)
    #중복제거
    for y in a:
        prime = 1
        if y != 1 and y != 0:
            for z in range(2,y):
                if y % z == 0:
                    prime = -1
                    break
            if prime == -1:
                pass
            else :
                answer+=1
    #소수판별
    return answer

solution('011')