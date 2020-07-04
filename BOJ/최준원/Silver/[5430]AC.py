'''
# 시간제한이 있기 때문에 pop(0)는 사용을 하지 않았다.
from sys import stdin,stdout
t = int(input())
for i in range(t):
    cmd = stdin.readline()
    t = int(stdin.readline())
    # str 형을 stdin으로 받을 때 마지막에 \n까지 받아오는 것을 감안해서 출력, 입력해야 한다.
    # 귀찮으니까 그냥 입력받은 형태를 list로 변환하자!
    arr = stdin.readline()
    xarr = []
    for i in arr:
        xarr.append(int(i))
    print(xarr)
    arr= list(arr.split(','))
    print(arr)
    xarr = []
    if arr == []:
        print('error')
        continue
    for i in arr:
        xarr.append(int(i))
    for i in cmd:
        if i == 'R':
            xarr = xarr[::-1]
        elif i == 'D':
            if xarr == []:
                print('error')
                break
            else:
                xarr = xarr[1:]
        else:
            print(xarr)
'''

# 너무 꼬여서 새롭게 머리를 비우고 시작. 출력 부분과 입력 부분에 신경을 쓰자. 출력에 sep=''를 사용해서 빈칸을 줄이고, 리스트 인풋 부분을 신경쓰자
# 두자릿수 원소를 받는 부분에서 자꾸 실수했다
from sys import stdin
t = int(input())
for i in range(t):
    cmd = stdin.readline()
    t = int(input())
    # 여기서 개행 부분도 처리
    arr = stdin.readline()[1:-2]
    arr = arr.split(',')
    res = []
    if arr == [''] and cmd[0] == 'D':
        print("error")
        continue
    for i in arr:
        res.append(int(i))
    for i in cmd:
        if i == 'R':
            res = res[::-1]
        if i == 'D':
            if res == []:
                print("error")
                break
            else:
                res = res[1:]
    print(''.join[i for i in res])


'''
1
RDD
4
[1,2,3,4]

1
DD
2
[42]

1
D
0
[]
'''