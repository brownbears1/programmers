"""
**한 번에 최대 2명**

최대 효율성은 가장 무거운 사람 + 가장 가벼운 사람
"""

from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0

    while people:
        escape = people.pop()
        if people and escape + people[0] <= limit:
            people.popleft()
        answer += 1

    return answer


# def solution(people, limit):
#     """
#     리스트를 보존하면서 구하는 방법
#     """
#     answer = 0
#     people.sort(reverse=True)
#     last_idx = len(people) - 1
#     for idx, weight in enumerate(people):
#         if weight + people[last_idx] <= limit:
#             last_idx -= 1
#
#         answer += 1
#
#         if idx >= last_idx:
#             break
#
#     return answer


assert solution([70, 50, 80, 50], 100) == 3
assert solution([70, 80, 50], 100) == 3
assert solution([40, 40, 80], 160) == 2

