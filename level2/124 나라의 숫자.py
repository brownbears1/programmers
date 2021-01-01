"""
표현할 수 있는 수가 (1,2,4) 3개밖에 없으므로 3진법으로 생각하면 쉽다.

1을 3으로 나눴을 때, 나온 나머지 1를 124 나라에선 1
2를 3으로 나눴을 때, 나온 나머지 2를 124 나라에선 2
3을 3으로 나눴을 때, 나온 나머지 0를 124 나라에선 4

여기서 계산을 할 때, 3의 경우 몫이 1이 되는데 이대로 계산을 한다면 14가 나온다.
0~2로 표현을 해야 하므로 값을 계산할 때, n - 1로 진행해준다. (n은 0 < n < 500,000,000 범위를 가짐)
"""

# from collections import deque
#
#
# def solution(n):
#     """
#     반복문 버전
#     """
#     custom_base = {
#         1: 1,
#         2: 2,
#         0: 4
#     }
#     result = deque()
#     while n:
#         n, r = divmod(n, 3)
#         if not r:
#             n -= 1
#         result.appendleft(str(custom_base[r]))
#
#     return ''.join(result)


def solution(n):
    """
    재귀함수
   계산할 때, n - 1로 진행하면 아래와 같은 순서를 가진 iterable한 값을 가질 수 있다
    n
    1 2 3
    n-1 한 결과를 3으로 나눈 나머지
    0 1 2

    변환되는 수
    1 2 4
    """
    if n == 0:
        return ''
    n, r = divmod(n-1, 3)

    return solution(n) + '124'[r]


assert solution(1) == '1'
assert solution(2) == '2'
assert solution(3) == '4'
assert solution(4) == '11'





















