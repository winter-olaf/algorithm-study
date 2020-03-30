# skill의 기준으로 정렬된 i와 그냥 정렬된 i를 비교하면 된다고 생각했으나...
# 그 방법을 몰라서 단순하게 코딩
def solution(skill, skill_tree):
    ans = 0

    for tree in skill_tree:
        tmp = ''
        # 반복문의 사용이 서툴러 자꾸 에러가 나서 참거짓 판별을 위한 변수 추가
        able = True
        
        # skill에 해당되는 스킬만 추출
        for t in tree:
            if skill.find(t) != -1:
                tmp += t
        # 모든 경우에 같을 때 가능하도록
        for i in range(len(tmp)):
            if skill[i] != tmp[i]:
                able = False
                break
        if able == True:
            ans += 1
            
    return ans
        
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
