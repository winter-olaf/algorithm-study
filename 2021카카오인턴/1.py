def solution(s):
    numdict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for str_key in numdict.keys():
        s = s.replace(str_key, numdict[str_key])
    return int(s)w