ans = [0]*10000
# 셀프넘버인지 체크
for i in range(10000):
    a = i//10000
    b = i//1000
    c = (i//100)%10
    d = (i//10)%10
    e = i%10
    res = i+(a+b+c+d+e)-1
    if res<=9999:
        ans[res] = 1
for i,v in enumerate(ans[0:10000]):
    if v == 0:
        print(i+1) # 인덱스 값이므로 1을 더해서 출력