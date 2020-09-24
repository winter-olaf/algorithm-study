# 틀린
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(input())
# cal =[]
# for i in arr:
#     count = 0
#     len_count = len(i)
#     while count < len(i):
#         cal.append((i[count], len_count))
#         count+=1
#         len_count-=1
# cal.sort(key= lambda x : x[1], reverse=True)

# done = {}
# num = 9
# for a,b in cal:
#     if a not in done:
#         done[a] = num
#         num-=1
# result = []
# for i in arr:
#     tmp = ''
#     for j in i:
#         tmp+=str(done.get(j))
#     result.append(tmp)
# res = 0
# for i in result:
#     res+=int(i)
# print(res)

n = int(input())
arr = []
chars = [0] * 26
for i in range(n):
    arr.append(list(input()))
for i in arr:
    for j in range(len(i)):
        chars[ord(i[j])-ord('A')] += 10**(len(i)-j-1)
chars.sort(reverse=True)

result = 0
for i in range(9, -1, -1):
    result += (chars[9-i]*i)
print(result)
    

'''
2
GCF
ACDEB

2
AAA
AAA
'''
