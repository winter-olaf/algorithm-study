c = int(input())
for _ in range(c):
    arr = list(map(int, input().split()))
    students = arr[0]
    scores = arr[1:]
    avg = '%.3f' % (sum(scores)/students)
    res = 0
    for i in scores:
        if i > float(avg):
            res+=1
    result = res/students
    print('%.3f' % (result*100)+'%')