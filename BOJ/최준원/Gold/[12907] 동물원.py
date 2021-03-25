N = int(input())
animals = list(map(int, input().split()))
flag = True

# 순서를 알아야 함
# animal_count = list(Counter(animals).values())
animal_count = [0] * 41

for animal in animals:
    animal_count[animal] += 1

if max(animals) >= N or max(animal_count) >= 3:
    flag = False

# 아! 이전에 나온 숫자의 개수보다 더 많은 개수가 나온다면 잘못된 경우다.
# 예제 5의 3, 1 0 1
max_cnt = animal_count[0]
for i in animal_count:
    if max_cnt < i:
        flag = False
        break
    max_cnt = i

if flag:
    cal = animal_count.count(2)
    if animal_count.count(1) != 0:
        cal += 1
    print(2**cal)
else:
    print(0)