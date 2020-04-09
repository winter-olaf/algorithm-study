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
    # [10, 50, 100]처럼 최하 value가 어떤 idx보다 클 경우 리스트의 길이 자체를 반환해야 함
    return lc
