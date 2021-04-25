"""
두 변수 중 가장 작은 수와 나머지 변수의 가장 큰 수를 곱해나가는 방향으로 진행하면 최소값을 구할 수 있다.

"""


def solution(A, B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))


assert solution([1, 4, 2], [5, 4, 4]) == 29
assert solution([1, 2], [3, 4]) == 10
