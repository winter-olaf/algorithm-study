#구현 방법 : 레이저를 나타내는 '()' 를 다른 문자로 변환하고,
#           남은 ()를 지워나가면서 갯수를 반환.
def solution(arg):
    ans = 0
    a = arg.replace('()','.')
    #print '.((..)(.).))(.)'

    while (True):
        cnt = 0
        idx = a.find('(.')
        # '(.'를 몾찾으면 break
        if idx == -1:
            break
        #찾은 idx 부터 '(' 와 ')'를 지워나감
        for idx2,i in enumerate(a[idx:]):
            #레이저를 만나면 cnt를 + 1
            if i == '.':
                cnt += 1
            else:
                ans += cnt + 1
                idx1 = idx + idx2 + 1
                a = a[:idx] + a[idx:idx1].replace("(","",1)+ a[idx1:].replace(")","",1)
                break
    return ans
#답이 제대로 안나옴.. 아마 괄호를 지울 때 제대로 안지워지는듯? 너무 복잡하게 풀어서 싹 다 지움


#구글을 참고해서 코딩을 하였다.
def solution(arg):
    ans = 0
    temp = 0
    last = "open"
    for i in arg:
        if i == '(':
            temp +=1
            last = "open"
        else:
            if last == 'open':
                #괄호가 열렸다 바로 닫힌 레이저
                temp -= 1
                ans += temp
                last = "close"
            else:
                temp -=1
                ans += 1
                #괄호의 끝부분
    return ans

print(solution('()(((()())(())()))(())'))