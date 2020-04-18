def solution(n):
    base = ['A']*len(n)
    ans = 0
    n = list(n)
    idx = 0

    while True:
        # 최단경로가 왼쪽으로 갈 때인지 오른쪽으로 갈 때인지 판단하기 위한 변수를 각각 생성
        rightidx = 1
        leftidx = 1
        # 같은 문자가 되면 break
        if n == base:
            break
        # 해당 문자가 A가 아닌 경우
        if n[idx] != 'A':
            # A의 아스키코드 값은 65 Z는 90으로 중간값이 13, 따라서 비교하는 문자에서 A를 뺐을 때의 값이 14 이상이라면 아래 방향키를 눌러서 해당 문자로 변환하는 것이 탐욕
            if ord(n[idx])-ord('A') >= 14:
                ans += 26 - (ord(n[idx])-ord('A'))
            # 반대의 경우는 위의 방향키를 누르는 것이 탐욕
            else:
                ans += ord(n[idx])-ord('A')
            n[idx] = "A"
        
        else:
            for i in range(1,len(n)):
                # 오른쪽과 왼쪽으로 각각 이동시키며 A가 아닌 것을 만날때까지의 길이 측정
                if n[idx-i] == 'A':
                    leftidx+=1
                else:
                    break
                if n[idx+i] == 'A':
                    rightidx+=1
                else:
                    break
            # 만약 오른쪽으로 이동하는 거리가 더 길다면
            if rightidx > leftidx:
                # 결과에 왼쪽으로 간 만큼의 idx를 더하고 왼쪽으로 갔으니 idx에서 뺌
                ans += leftidx
                idx -= leftidx
            else:
                ans += rightidx
                idx += rightidx
    return ans