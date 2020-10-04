n = int(input())
answer = 0
def check(word):
    stack = []
    for i in word:
        if i not in stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.append(i)
            else:
                return False
    return True

for _ in range(n):
    word = list(input())
    if check(word):
        answer+=1
print(answer)