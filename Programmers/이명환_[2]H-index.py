
def solution(citations):
    for idx,i in enumerate(sorted(citations)):
       if i>= len(citations) -i:
           return len(citations)-i
    return 0