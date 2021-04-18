from collections import deque

def isgood(Q):
    stack = []
    key = {')':'(', '}':'{', ']':'[' }
    for q in Q:
        if q in [')', '}', ']']:
            if stack:
                if stack[-1] == key[q]:
                    stack.pop()
                else:
                    stack.append(q)
            else:
                stack.append(q)
        else:
            stack.append(q)

    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    queue = deque()

    for c in s:
        queue.append(c)

    if isgood(queue):
        answer += 1

    for x in range(len(s)-1):
        queue.append(queue.popleft())
        if isgood(queue):
            answer += 1

    return answer

print(solution("[](){}"))