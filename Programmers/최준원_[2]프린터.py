def solution(p,l):
    
    ans, cnt = 0, 0
    # 비교를 위한 정렬된 리스트
    tmp = sorted(p,reverse=True)
    while True:
        # Index 기억을 위해서 enumerate를 사용
        for idx, pt in enumerate(p):
            # max(p)를 만날 때까지 index와 pt를 하나씩 증가시키면서 비교하기
            prior = tmp[cnt]
            # 같아졌을 때, 카운트를 하나씩 올리며 비교
            if pt == prior:
                cnt+=1
                ans+=1
                # 인덱스가 같으면 return
                if idx == l:
                    return ans
        # return을 못만나면 다시 반복
        else:
            continue

print(solution([2, 1, 3, 2],2))