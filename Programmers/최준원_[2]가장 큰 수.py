def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


# 설명이 잘 되어있는 다른 방식을 추가함
from functools import reduce
lst=sorted(input("여러가지 숫자를 입력하십시오: ").split(",")) #3,34,30,5,9 ->["3","30","34","5","9"]
f=lambda x, y : max(x+y,y+x)
print(reduce(lambda x, y : x+y, lst)) #3303459 #((((3+30)+34)+5)+9)
print(reduce(lambda x, y : y+x, lst)) #9534303 #(9+(5+(34+(30+3))))
print(reduce(f, lst)) #9534330   #max((3+30),(30+3)) -> x=330, y=다음 시퀀스 값
                                        #max((330+34),(34+330)) -> x=34330,
                                        #max((34330+5),(5+34330)) -> x=534330,
                                        #max((534330+9),(9+534330)) -> x=9534330


#만약 큰 수가 아니고 작은 수일 경우
#min((3+30),(30+3)) -> x=303
#min((303+34),(34+303)) -> x=30334
#min((30334+5),(5+30334)) -> x=303345
#min((303345+9),(9+303345)) -> x=3033459

print(solution([3, 530, 34, 5, 9]))