def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    list1, list2 = [], []

    for i in range(len(str1)-1):
        if ord('a') <= ord(str1[i]) <= ord('z') and ord('a') <= ord(str1[i+1]) <= ord('z'):
            list1.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if ord('a') <= ord(str2[i]) <= ord('z') and ord('a') <= ord(str2[i + 1]) <= ord('z'):
            list2.append(str2[i:i+2])

    inter = 0
    for c in list1:
        if c in list2:
            inter += min(list1.count(c), list2.count(c))

    union = len(list1) + len(list2) - inter

    print(union, inter)

    answer = 65536 if union == 0 or inter == 0 else int((inter/union)*65536)
    return answer

# print(solution('FRANCE', 'french'))
# print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('aa1+aa2', 'AAAA12'))
# print(solution("AAbbaa_AA", 'BBB'))