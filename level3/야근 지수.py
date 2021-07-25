"""
sort로도 풀릴 줄 알았는데 효율성에서 실패남.
아무래도 sort는 O(NlogN)이라 그런거 같다.
heap의 경우, 트리를 재구성할 때, 트리의 높이만큼 시간복잡도가 발생하므로 O(logN)이라 일반 정렬보다 빠르다.
"""
# def solution(n, works):
#     """
#     효율성 시간초과
#     """
#     if n >= sum(works):
#         return 0
#     for _ in range(n):
#         works.sort()
#         works[-1] -= 1
#     return sum(map(lambda x: x**2, works))
#

import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    heapq._heapify_max(works)
    for _ in range(n):
        heapq._heapreplace_max(works, works[0] - 1)

    return sum(map(lambda x: x**2, works))


assert solution(4, [4, 3, 3]) == 12
assert solution(1, [2, 1, 2]) == 6
assert solution(3, [1,1]) == 0
