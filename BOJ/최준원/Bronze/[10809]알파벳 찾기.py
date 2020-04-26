import string
n = input()
arr = [n.find(x) for x in string.ascii_lowercase]
for i in arr:
    print(i,end=' ')

# 다른 풀이
import string
n = input()
for i in string.ascii_lowercase:
    print(n.find(i),end=' ')

# 다른사람 풀이
print(*map(input().find,map(chr,range(97,123))),sep=" ")