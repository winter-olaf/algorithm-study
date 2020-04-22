import sys
arr = []
for i in range(9):
    # sys.stdin은 ^Z를 입력받으면 종료해 준다.
    arr.append(int(sys.stdin.readline()))
print(max(arr),arr.index(max(arr))+1,sep='\n')
