def solution(n):
    ans = 0
    # bin 함수를 사용하면 str 형으로 반환된다는 것을 알았음.
    # If using index slice[2:], we can show nums without 0b
    one = bin(n).count('1')
    print(type(bin(n)))
    for i in range(n+1,1000001):
        if bin(i).count('1') == one:
            ans = i
            break
    return ans

# 가장 간단하게 풀어봄
def solution(n):
    one = bin(n).count('1')
    for i in range(n+1,1000001):
        if bin(i).count('1') == one:
            return i
print(solution(78))
