# 93.8/100
def solution(citations):
    citations.sort(reverse=True)
    lc = len(citations)
    for i, j in enumerate(citations):
        if i >= j:
            return i
    
# 100/100
def solution(citations):
    citations.sort(reverse=True)
    lc = len(citations)
    for i, j in enumerate(citations):
        if i >= j:
            return i
    # [10, 50, 100]처럼 최하 value도 
    return lc
