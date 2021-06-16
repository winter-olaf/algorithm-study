def solution(n, k, cmds):
    answer = ''
    result = [True]*n # False일 경우 삭제되었음을 뜻함
    cur = k # 현재 선택된 행
    undo_stack = []

    for cmd in cmds:
        if cmd[0] in ['D', 'U']:
            d = int(cmd[2]) # 이동해야 하는 행
            move = 1 if cmd[0] == 'D' else -1
            cnt = 0
            while cnt != d:
                cur += move
                if result[cur]:
                    cnt += 1

        elif cmd[0] == 'C':
            # 행 삭제
            result[cur] = False
            undo_stack.append(cur)

            # 삭제 이후 행 변화
            # 마지막 행인가?
            is_last = True
            # 자기 뒤에 살아 있는 행이 있다면 그곳이 현재 행
            for i in range(cur, n):
                if result[i]:
                    cur = i
                    # 마지막 행이 아니었음
                    is_last = False
                    break
            # 현재가 맨 마지막 행인 경우, 자기 위의 행을 선택해야 함
            # (cur 뒤의 행이 모두 False인 경우)
            if is_last:
                for i in range(cur-1, -1, -1):
                    if result[i]:
                        cur = i
                        break
        else: # undo
            result[undo_stack.pop()] = True

    for i in result:
        if i:
            answer += 'O'
        else:
            answer += 'X'

    return answer

print(solution(5,4, ['C','U 3', 'C']))