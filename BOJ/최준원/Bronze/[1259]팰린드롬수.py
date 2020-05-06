# # 백준식이면 매 줄마다 출력해도 되겠지?
# # 역시 맞는군...
# while True:
#     n = input()
#     if n == '0':
#         break
#     elif n == n[::-1]:
#         print("yes")
#     else:
#         print("no")
# Short Coding
# pypy3에서 내가 제일 짧음
while True:
    n=input()
    if n=='0':
        break
    # print('yes'if n==n[::-1] else 'no')
    # 다른 출력법
    print(['no','yes'][n==n[::-1]])

# python3 1위의 예술적인 풀이
S=input()
while S!='0':print('yneos'[S!=S[::-1]::2]);S=input()