def solution(n):
    bina = format(n,'b')
    temp = n
    while (True):
        if format(temp+1,'b').count('1') == bina.count('1'):
            return temp+1
        temp +=1