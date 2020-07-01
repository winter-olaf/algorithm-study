from itertools import combinations
from sys import stdin

while True:
    t = list(map(int,stdin.readline().split()))
    a = []
    if t[0] == 0:
        break
    for i in combinations(t[1:],6):
        for j in i:
            print(j,end=" ")
        print("")
    # 출력 형식이 잘못되었습니다...ㅡㅡ
    # end 옵션을 추가하니까 통과
    # end 옵션의 default가 newline(개행)이므로, \n을 프린트 할때 end 처리를 하지 않으면 개행이 두 단 되는 문제를 확실히 파악함
    print('\n',end='')