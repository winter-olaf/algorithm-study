import sys

n = int(sys.stdin.readline())
students = []
for _ in range(n * n):
    students.append(list(map(int, sys.stdin.readline().split(' '))))
class_room = list([0 for _ in range(n)] for j in range(n))
coordinate = [(1, 0), (-1, 0), (0, -1), (0, 1)]

for k in range(n * n):
    student = students[k][0]
    # 1. 비어있는 칸중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
    favorite_coordinate = []
    step2 = []
    step3 = []
    favorite = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if class_room[i][j] == 0:
                # 인접칸 좋아하는 학생 확인
                cnt = 0
                for z in range(4):
                    y, x = coordinate[z]
                    if 0 <= i + y < n and 0 <= j + x < n:
                        if class_room[i + y][j + x] in students[k][1:]:
                            cnt += 1
                favorite_coordinate.append([cnt, i, j])
    favorite = max(favorite_coordinate)
    for i in range(len(favorite_coordinate)):
        if favorite_coordinate[i][0] == favorite[0]:
            step2.append(favorite_coordinate[i])


    empty_blank = []
    #2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    if len(step2)==1:
        class_room[step2[0][1]][step2[0][2]] = student
    else:
        cnt = 0
        for p in range(len(step2)):
            i = step2[p][1]
            j = step2[p][2]

            # 인접칸 비어있는 칸 확인
            cnt = 0
            for z in range(4):
                y, x = coordinate[z]
                if 0 <= i + y < n and 0 <= j + x < n:
                    if class_room[i + y][j + x] ==0:
                        cnt += 1
            empty_blank.append([cnt, i, j])
        blank = max(empty_blank)
        for i in range(len(step2)):
            if empty_blank[i][0] == blank[0]:
                step3.append(empty_blank[i])


    #3 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        class_room[step3[0][1]][step3[0][2]] = student

#만족도 구하기

satisfaction = 0
while(students):
    student = students.pop()
    cnt =0
    for i in range(n):
        for j in range(n):
            if class_room[i][j] == student[0]:
                for z in range(4):
                    y, x = coordinate[z]
                    if 0 <= i + y < n and 0 <= j + x < n:
                        if class_room[i + y][j + x] in student[1:]:
                            cnt += 1
    if cnt == 0:
        pass
    elif cnt ==1:
        satisfaction += 1
    elif cnt ==2:
        satisfaction += 10
    elif cnt ==3:
        satisfaction += 100
    elif cnt == 4:
        satisfaction += 1000
print(satisfaction)