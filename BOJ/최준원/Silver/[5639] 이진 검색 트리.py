from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def postorder(start, end):
    if start > end:
        return
    root = data[start]
    cut = end + 1

    for i in range(start+1, end+1):
        if root < data[i]:
            cut = i
            break

    postorder(start+1, cut-1)
    postorder(cut, end)
    print(root)

cnt = 0
data = []

while cnt <= 10000:
    try:
        data.append(int(stdin.readline()))
    except:
        break
    cnt += 1

postorder(0, len(data)-1)