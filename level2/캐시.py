from collections import deque


def solution(cacheSize, cities):
    answer = 0
    caches = deque(maxlen=cacheSize)

    if not cacheSize:
        return len(cities) * 5

    for i, city in enumerate(cities):
        city = city.lower()
        if city in caches:
            answer += 1
            caches.remove(city)
        else:
            answer += 5
        caches.append(city)

    return answer


assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50
assert solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21
assert solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60
assert solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 52
assert solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16
assert solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25
