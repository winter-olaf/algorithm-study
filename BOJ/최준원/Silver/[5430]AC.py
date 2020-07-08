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
# 스택과 예외처리를 이용해서 인풋을 받자
# 시간초과;; 50%까지 됐는데 까비
# from sys import stdin,stdout
# t = int(stdin.readline())
# for i in range(t):
#     cmd = stdin.readline()
#     t = int(stdin.readline())
#     arr = stdin.readline()
#     res = []
#     num = ''
#     for i in arr:
#         if i not in [',','[',']'] :
#            num+=i
#         elif num != '':
#             res.append(int(num))
#             num = ''

#     for i in cmd:
#         if i == 'R':
#             res = res[::-1]
#         if i == 'D':
#             if res == []:
#                 print("error")
#                 break
#             else:
#                 res = res[1:]
#     if res == []:
#         continue
#     result = ''
#     for i in res:
#         result+=str(i)
#     stdout.write('['+','.join(result)+']')

# 뒤집는 연산을 하지 않도록 flag를 두고 안뒤집어졌을땐 슬라이싱, 뒤집어졌을때는  pop을 하도록 처리
# 런타임 에러. 걍 다시 풀자... 목디스크땜에 집중이 안되네 ㅠㅠ
'''
from sys import stdin,stdout
t = int(stdin.readline())
for i in range(t):
    cmd = stdin.readline()
    t = int(stdin.readline())
    arr = stdin.readline()
    res = []
    num = ''
    d_cnt = 0
    r_cnt = 0
    for i in arr:
        if i not in [',','[',']'] :
           num+=i
        elif num != '':
            res.append(int(num))
            num = ''
    for i in cmd:
        if i == 'R':
            r_cnt+=1
        elif i == 'D':
            if r_cnt%2 == 0: # 리스트가 뒤집어지지 않았을 경우
                d_cnt+=1
            else:
                res.pop()
    if r_cnt%2 == 1:
        res = res[::-1]
    if len(res) < d_cnt:
        stdout.write("error")
        continue
    else:
        res = res[d_cnt:]
    result = ''
    stdout.write('[')
    for i in range(len(res)):
        if i == len(res) - 1:
            print(res[i],end='')
        else:
            print("%d," %res[i],end='')
    stdout.write(']')
'''
# 또 틀림. 뭐가 문제일까? 왜 이게 안되는건데?
# 개행 문제였다. 아 이건 출력 형식이 개 오바지 ㅡㅡㅡ
# print로 하니까 그냥 해도 되는데 stdout으로 할때는 각 return 값마다 \n을 붙여 줘야 한다.
from sys import stdin, stdout
def AC(cmd,n,arr):
    r,p,s = 0,0,0
    for c in cmd:
        if c == 'R':
            r+=1
        elif c == 'D':
            if r%2==0:
                s+=1 # 안뒤집었을 때는 slicing
            else:
                p+=1 # 뒤집었을 때는 pop
    if s+p <= n:
        arr = arr[s:n-p]
        if r%2 == 0: return '['+','.join(arr)+']' # 뒤집
        else: return '['+','.join(arr[::-1])+']' #안뒤집
    else:
        return 'error'
t = int(stdin.readline())
for _ in range(t):
    cmd = stdin.readline()
    n = int(stdin.readline())
    arr = stdin.readline()[1:-2].split(',')
    if n == 0:
        arr = []
    print(AC(cmd,n,arr))