# 내 풀이
n = int(input())
def solution(n):
    ans = ''
    while(n>0):
        if n%3 == 0:
            ans += "4"
            n = int(n/3)-1
        else:
            ans += str(n%3)
            n = int(n/3)
    return ans[::-1]
print(solution(n))

# 다른 사람의 풀이

def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer