def solution(records):
    answer = []
    userName = {}

    # 딕셔너리에 추가
    for record in records:
        tmp = record.split()
        # 들어올 때와 변경할 때만 고려하면 된다.
        if tmp[0] in ['Enter', 'Change']:
            userName[tmp[1]] = tmp[2]

    for record in records:
        tmp = record.split()
        nick = userName[tmp[1]]
        if tmp[0] == 'Enter':
            answer.append(f'{nick}님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(f'{nick}님이 나갔습니다.')

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])