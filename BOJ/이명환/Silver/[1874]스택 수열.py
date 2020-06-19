import sys
n = int(sys.stdin.readline())
input_arr =[]
program_arr = [1]
oper_arr = ['+']
input_idx = 0
num = 2
can_arr = True
for i in range(n):
    input_arr.append(int(sys.stdin.readline()))
while(input_idx<n):
    if (program_arr == [] or program_arr[-1] < input_arr[input_idx]):
        program_arr.append(num)
        oper_arr.append('+')
        num += 1
    else:
        temp = program_arr.pop()
        oper_arr.append('-')
        if (temp != input_arr[input_idx]):
            can_arr = False
            break
        input_idx +=1
if can_arr:
    for i in oper_arr:
        print(i)
else:
    print('NO')