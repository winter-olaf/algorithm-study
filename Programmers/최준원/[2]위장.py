from collections import Counter,defaultdict
def solution(clothes):
    result = 1
    # 의상을 하나만 껴도 되기 때문에 리스트를 [' ','yellow_hat'] 이런 식으로 조합한 뒤,
    # ['','',''] 이런 식으로 하나도 안입는 경우는 딱 한개가 나오니까 그걸 제거하면 된다.
    able = Counter([k for v,k in clothes])
    for i in able:
        result *= (able[i]+1)
    result -= 1    
    return result
    
print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
