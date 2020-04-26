arr = []
for i in range(10):
    arr.append(int(input())%42)
print(len(set(arr)))

# Oneline Code
print(len(set(eval("int(input())%42,"*10))))
##
print(len({int(input())%42 for _ in range(10)}))