def solution(s):
    max_len = 0
    end = len(s)
    for i in range(end):
        idx = end-1
        while idx >= i:
            if s[i] == s[idx]:
                if s[i:idx+1] == s[i:idx+1][::-1]:
                    if max_len < len(s[i:idx+1]):
                        max_len = len(s[i:idx+1])
            idx -= 1
    return max_len

# 큰 회문부터 줄이자
def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i