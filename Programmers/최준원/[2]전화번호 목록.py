# 84.6/100 
# 테스트 8,9 실패
# startwith()이라는 함수가 있음!
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            if j.startswith(phone_book[i]) or phone_book[i].startswith(j):
                return False
    return True

# 통과!
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            # 뒤의 것으로 앞 번호가 시작되는 경우를 깜빡했다
            if j.startswith(phone_book[i]) or phone_book[i].startswith(j):
                return False
    return True

print(solution(['1195524421', '97674223', '119']))
