import sys
import heapq

t = int(sys.stdin.readline())

for i in range(t):
    N, M = map(int, sys.stdin.readline().split())
    books = [k for k in range(1, N + 1)]
    answer = 0
    apllication = []
    for m in range(M):
        a, b = map(int, sys.stdin.readline().split())
        heapq.heappush(apllication, (b, (a, b)))
    while (apllication and books):
        a, b = heapq.heappop(apllication)[1]
        for num in range(a, b + 1):
            if num in books:
                books.remove(num)
                answer += 1
                break
    print(answer)

# a 기준으로 sort 안해도 되는듯?