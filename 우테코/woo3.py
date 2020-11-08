def solution(money, e, a):
    base = 100
    for i in range(len(e)):
        money -= base
        if e[i] == a[i]:
            money += base * 2
            base = 100
        elif e[i] != a[i]:
            base *= 2
            if base >= money:
                base = money
    return (money)