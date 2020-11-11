def solution(s):
    zero, count = 0, 0
    num = s[:]
    while num != "1":
        stack = []
        count+=1
        for i in num:
            if i=='1':
                stack.append(i)
            else:
                zero+=1
        num = ''.join(stack)
        num = str(bin(len((num))))[2:]
    return ([count, zero])
print(solution("110010101001"))
