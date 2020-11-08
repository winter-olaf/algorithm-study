logs = 	["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]

def solution(logs):
    data = {}
    for i in logs:
        student, problem, score = i.split(' ')
        if (student not in data):
            data.setdefault(student, {})[problem] = score
        else:
            data[student][problem] = score
    for key in list(data.keys()):
        if len(list(data[key].values())) < 5:
            del data[key]
    result = []
    students = list(data.keys())
    for i in range(len(students)):
        i_solved = list(data[students[i]].items())
        for j in range(i + 1, len(students)):
            count = 0
            j_solved = list(data[students[j]].items())
            for i_s in i_solved:
                for j_s in j_solved:
                    if (i_s[0] == j_s[0] and i_s[1] == j_s[1]):
                        count+=1
            if count >= 5:
                result.append(students[i])
                result.append(students[j])
    if result == []:
        return ["None"]
    return sorted(list(set((result))))
print(solution(logs))