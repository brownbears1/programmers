"""
최악의 경우, 다리 길이: 10000 지탱무게: 1, 트럭의 수: 10000이 될 수 있어 재귀로는 풀기 어려움
list의 insert()는 O(n), pop()은 가장 마지막 index를 제외하고 O(n)으로 deque를 사용한다.
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 1
    truck_weight_sum = 0
    truck_weights = deque(truck_weights)
    crossing_trucks = deque()

    while truck_weights or crossing_trucks:
        if truck_weights and truck_weight_sum + truck_weights[0] <= weight:
            crossing_trucks.append([truck_weights.popleft(), bridge_length])
            truck_weight_sum += crossing_trucks[-1][0]

        for i in range(len(crossing_trucks)):
            crossing_trucks[i][1] -= 1

        if not crossing_trucks[0][1]:
            truck_weight_sum -= crossing_trucks.popleft()[0]
        time += 1

    return time


assert solution(2, 10, [7, 4, 5, 6]) == 8
assert solution(100, 100, [10]) == 101
assert solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110
assert solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]) == 19
