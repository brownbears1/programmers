"""
완전탐색, 깊이 우선 탐색, 너비 우선 탐색 어떤 알고리즘을 사용해서 풀던 시간 복잡도는 전부 O(n^2)
"""


from itertools import product


# def solution(numbers, target):
#     """
#     카테지안 곱을 사용한 완전 탐색
#     """
#     return list(map(sum, product(*[(x, -x) for x in numbers]))).count(target)


# import collections
#
#
# def solution(numbers, target):
#     """
#     bfs(queue)
#     """
#     answer = 0
#     queue = collections.deque([(0, 0)])
#     while queue:
#         current_sum, num_idx = queue.popleft()
#
#         if num_idx == len(numbers):
#             if current_sum == target:
#                 answer += 1
#         else:
#             number = numbers[num_idx]
#             queue.append((current_sum + number, num_idx + 1))
#             queue.append((current_sum - number, num_idx + 1))
#
#     return answer


def solution(numbers, target):
    """
    dfs(stack)
    """
    def dfs(idx, value):
        if idx == n:
            if target == value:
                return 1
            return 0

        return dfs(idx + 1, value + numbers[idx]) + dfs(idx + 1, value - numbers[idx])

    n = len(numbers)
    return dfs(0, 0)


assert solution([1, 1, 1, 1, 1], 3) == 5
