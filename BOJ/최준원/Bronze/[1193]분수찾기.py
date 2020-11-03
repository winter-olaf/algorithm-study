# 0.5s Time limit
x, row, end = int(input()), 0, 0
while x>end:
    row+=1
    end+=row
a = end - x
if row%2 == 0:
    print(f'{row-a}/{a+1}')
else:
    print(f'{a+1}/{row-a}')