# String
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
nums = input()
res = 0
for i in nums:
    for j,val in enumerate(dial):
        if i in val:
            res+=(j+3)
print(res)