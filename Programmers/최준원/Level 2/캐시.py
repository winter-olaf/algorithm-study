from collections import deque
def solution(cacheSize, cities):
    answer = 0
    Q = deque()

    if cacheSize:
        for city in cities:
            city = city.lower()
            if city in Q:
                Q[-1], Q[Q.index(city)] = Q[Q.index(city)], Q[-1]
                # Q.remove(city)
                # Q.append(city)
                answer += 1
            else:
                if len(Q) >= cacheSize:
                    Q.popleft()
                Q.append(city)
                answer += 5
    else:
        answer += 5 * len(cities)

    return answer
