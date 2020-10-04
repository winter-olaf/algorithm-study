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
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia:
    words = words.replace(i,'!')
print(len(words))