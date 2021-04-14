def solution(n, lost, reserve):
    reserve = [x for x in reserve if x not in lost]
    lost = [y for y in lost if y not in reserve]
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
            print(lost)
        elif i+1 in lost:
            lost.remove(i+1)
            print(lost)
    return n-len(lost)

# # 이건 되는데 위에건 안된다고?
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)

print(solution(5,[2,4],[1,3,5]))
