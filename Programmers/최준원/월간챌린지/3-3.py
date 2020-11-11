import collections

def solution(a):
    c = collections.Counter(a)
    var = 0
    mc = c.most_common()
    max_num = mc[0][1]
    for (x, y) in mc[1:]:
        var+=y
    if (max_num <= var):
        return (max_num * 2)
    else:
        return ((max_num - 2) * 2)
print(solution([0,3,3,0,7,2,0,2,2,0]))
