## 30.0/100.0
## 보트 부분을 보완해서 코드를 짜야겠군
# def solution(people, limit):
#     boat = 0
#     ans = 0
#     people = sorted(people,reverse=True)
#     while people:
#         # 보트에 사람 태움
#         if boat + people[-1] <= limit:
#             boat += people.pop()
#         # 보트가 꽉 차서 구출
#         else:
#             if boat + people[-1] == limit:
#                 people.pop()
#                 ans += 1
#                 boat = 0
#             elif boat + people[-1] > limit:
#                 ans += 1
#                 boat = 0
#     # 마지막에 보트에 타 있지만 100kg이 넘지 않는 경우
#     ans += 1
#     return ans

## 0.0/100 실환가??????? 
# def solution(people, limit):
#     boat = 0
#     ans = 0
#     people = sorted(people, reverse=True)
#     while people:
#         if boat + people[-1] < limit:
#             boat += people.pop()
#         elif boat + people[-1] == limit:
#             people.pop()
#             ans += 1
#             boat = 0
#         else:
#             ans += 1
#             boat = 0
#     if boat != []:
#         ans += 1
#     return ans
        
# pop을 쓰면 효율성 부분에서 틀려먹는 것 같다 흠
# 아 잘못 생각했다. max + min <= limit인 경우에 최선의 경우의 수가 나온다.
def solution(people, limit):
    people.sort()
    min_idx, max_idx = 0, len(people)-1
    iltaepi = 0
    while min_idx < max_idx:
        if people[min_idx] + people[max_idx] <= limit:
            iltaepi += 1
            min_idx += 1
            max_idx -= 1
        else:
            max_idx -= 1
    return len(people) - iltaepi
    
print(solution([70, 50, 80, 50],100))
