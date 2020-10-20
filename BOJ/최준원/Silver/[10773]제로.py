stack = []
for _ in range(int(input())):
    e = int(input())
    if e == 0:
        stack.pop()
    else:
        stack.append(e)
print(sum(stack))