from itertools import permutations

#고민하다가 도저히 어떻게 풀지 몰라서 구글에서 보았다..
#전체 경우의 수를 조합해서 (get_candidates) 조합한 숫자와
#주어진 숫자의 스트라이크와 볼의 갯수가 일치하는지 확인한다.(check_candidate,check)
#그리고 조건을 모두 만족하는 경우의 수 만큼 answer을 더한다.

LENGTH = 3

def solution(baseball):
    candidates = get_candidates(LENGTH)
    #가능한 경우의 수를 전부 구한 것을 리스트로 받음.
    answer_count = 0
    for candidate in candidates:
        is_passed = check_candidate(baseball, candidate)
        #각각의 경우의 수를 check_candidate 함수로 검증
        if is_passed:
            answer_count += 1
            #검증을 통과하면 answer값 +1
    return answer_count

def get_candidates(lenth):
    numbers = list(range(1,10))
    candidates = list(permutations(numbers,lenth))
    return candidates

def check_candidate(baseball, candidate):
    is_passed = True
    for guess in baseball:
        correct = check(guess, candidate)
        #여러개의 baseball(숫자,스트라이크,볼)과 모두 일치하는 후보 검증
        if not correct:
            is_passed = False
            break
            #하나라도 다르면 is_passed 에 False 값을 주고 break
    return is_passed

def check(guess,camdidates):
    guess_num,guess_strike ,_guess_ball =guess
    #guess = (숫자,스트라이크 갯수, 볼 갯수)
    candidate_str = tuple_to_str(candidates)
    #candidate = (1,2,3) or (2,3,4)......
    strike = 0
    ball = 0
    for str1,str2 in zip(guess_num_str,candidate_str):
        if str1 == str2:
            strike +=1
            #zip(*iterables) 두개의 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수
        elif str1 in candidate_str:
            ball+=1

    is_correct = True
    if strike != guess_strike or ball != _guess_ball:
        is_correct = False
        #검증한 strike 와 ball의 갯수가 일치하지 않는다면 is_correct에 False값을 준다.
    return is_correct

def tuple_to_str(tuple_):
    result = ""
    for number in tuple_:
        result += str(number)
    return result

#아직 문제를 풀 때 구조화(여러가지 기능을 구상하는 것) 능력이 많이 부족한 것 같다.
#조금 복잡한 문제는 함수를 여러개로 나눠서 푸는 것을 생각해야겠다.


solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])