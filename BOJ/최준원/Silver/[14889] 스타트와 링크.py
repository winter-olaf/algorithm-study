N = int(input())
data = [list(map(int, input().split())) for x in range(N)]
selected = [0]*N
start = 0
link = 0

def comb(idx, cnt):
    global start, link

    if cnt == N//2:
        # for i in range(N):
        #     if selected[i]:
        #         start += data[]
        print(selected)
        return

    if idx > N:
        return

    selected[idx] = 1
    comb(idx+1, cnt+1)
    selected[idx] = 0
    comb(idx, cnt+1)

comb(0, 0)