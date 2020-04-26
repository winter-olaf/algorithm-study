def solution(b,r):
    # x축 y축을 생각하면 전체 크기가 x*y이고 red 크기는 (x-2)(y-2)임을 알 수 있다.
    # 계산해보면 2x^2 - (brown+4)x + 2red + 2brown = 0
    # x = -b + sqrt(b^2-4ac)/2a (근의 공식)으로 계산
    # 방정식 형변환은 첨부한 [2]카펫 풀이.pdf 확인
    x = ((b+4) + ((b+4)**2 - 16*(b+r))**0.5)/4
    y = (b+r)//x
    return [x,y]