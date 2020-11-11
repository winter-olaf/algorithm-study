def solution(s, op):
    result = []
    for i in range(1, len(s)):
        a = int(s[0:i])
        b = int(s[i:])
        if op == "+":
            result.append(a+b)
        elif op == "-":
            result.append(a-b)
        elif op == "*":
            result.append(a*b)
    return (result)