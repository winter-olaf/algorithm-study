'''
틀림
words = input()
res, count, words_length = 0, 0, len(words)
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# 크로아티아 알파벳 계산
for i in croatia:
    if i in words:
        count+=(len(i)*words.count(i))
        res+=words.count(i)
        # words = words.replace(i,'')
        # replace를 하면 nljj같은 경우 lj가 삭제되고 nj를 계산해 버려서 답이 2가 되어 버린다.

# 예외 처리
if 'dz=' in words:
    val = words.count('z=')-words.count('dz=')
    res -= val
    count -= 2*val

# 입력받은 단어에서 크로아티아 알파벳의 길이를 차감한 뒤 결과값에 더한다.
res+=(words_length-count)
print(res)
'''
words = input()
count, words_length = 0, len(words)
croatia = ['c=','c-','d-','lj','nj','s=','z=']
result = [0]*7

# 크로아티아 알파벳 계산
for i,v in enumerate(croatia):
    if v in words:
        result[i]+=words.count(v)
if 'dz=' in words:
    count+=words.count('dz=')

val1 = (sum(result) - (result[-1]-count))
val2 = words_length - (2*val1 + 3*count)

print(val1+val2+count)