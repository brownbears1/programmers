"""
효율성 검사가 없어서 딱히 heapq를 안써도 됨
"""


# from collections import deque
#
#
# def solution(operations):
#     """
#     queue를 사용해 해결한 방식
#     """
#     answer = []
#
#     for operation in operations:
#         op, num = operation.split(' ')
#
#         if op == 'I':
#             answer.append(int(num))
#             answer = deque(sorted(answer, reverse=True))
#         else:
#             if not answer:
#                 continue
#             if num == '1':
#                 answer.popleft()
#             else:
#                 answer.pop()
#
#     return [0, 0] if not answer else [answer[0], answer[-1]]


import heapq


def solution(operations):
    """
    heap 사용한 방식
    """
    answer = []
    for operation in operations:
        op, num = operation.split(' ')

        if op == 'I':
            heapq.heappush(answer, int(num))
        else:
            if not answer:
                continue
            if num == '1':
                heapq._heapify_max(answer)
                heapq._heappop_max(answer)
            else:
                heapq.heapify(answer)
                heapq.heappop(answer)

    answer.sort()
    return [0, 0] if not answer else [answer[-1], answer[0]]


assert solution(["I 16", "D 1"]) == [0, 0]
assert solution(["I 7", "I 5", "I -5", "D -1"]) == [7, 5]
assert solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]) == [333, -45]