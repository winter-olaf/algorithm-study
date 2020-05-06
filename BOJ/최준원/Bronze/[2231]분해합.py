# # 완전탐색 문제인가?
# # eval을 사용한다면 시스템 명령을 입력받았을 때 Command Injection Flaws가 노출될 수 있다는 취약점을 기억하자
# # 시스템 명령을 삽입할 수 있는 스크립트 언어(php, js 등)이 공통적으로 가지는 취약점

# # 시간 초과
# n = int(input())
# tmp = []
# for x in range(1,n+1):
#     a = x + eval('+'.join(str(x)))
#     if (a) == n:
#         tmp.append(x)
# print([min(tmp),0][tmp==[]])

# # 단순하게 풀어보기
# # 이것도 안됨. 완전 탐색 자체가 시간 초과인가?
# n = int(input())
# tmp = []
# for x in range(1, n+1):
#     a = x + eval('+'.join(str(x)))
#     if (a) == n:
#         tmp.append(x)
# if tmp == []:
#     print(0)
# else:
#     print(sorted(tmp)[0])

# eval 말고 sum_digit을 써보자
# Runtime ERRRRRRRRRRR-!
# def sum_digit(n):
#     return sum(map(int, n))
# n = int(input())
# tmp = []
# for x in range(1,n+1):
#     if  x + sum_digit(str(x)) == n:
#         tmp.append(x)
# print([min(tmp), 0][tmp == []])

# if 문에서 비교할 것이 적도록 코딩
# 생각해보니 모든 경우를 구할 필요가 없다
# 드디어 통과
def sum_digit(n):
    s = sum(map(int, n))
    a = int(n) + s
    return a
n = int(input())
for x in range(1, n+1):
    if sum_digit(str(x)) == n:
        print(x)
        break
    if x == n:
        print(0)

# 숏코딩 2위
n = int(input())
for i in range(n):
	t = j = i
	while j:
	t += j % 10
	j //= 10
	if t == n:
	break
print(i if t == n else 0)
