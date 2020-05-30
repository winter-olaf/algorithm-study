nums = [3, 3, 3, 2, 2, 4]

def solution(nums):
    nl = len(nums)//2
    if len(set(nums)) >= nl:
        return nl
    else:
        return len(set(nums))

print(solution(nums))
