"""
해결법 1: 피보나치
1, 2, 3, 5, 8, 13, 21, ....
1, 2, 3, 4, 5, 6,  7, ....

피보나치의 경우, 1, 1, 2, 3, 5, 8, 13, 21, ... 순으로 나가는데 위 문제는 첫 번째가 생략되었으므로 주어진 문제에 1을 더한다.

해결법 2: 조합의 합
문제를 5까지 쭉 나열하면 규칙성이 보인다.
1
    1
2
    1 1
    2
3
    1 1 1
    2 1
    1 2
4
    1 1 1 1
    2 1 1
    1 2 1
    1 1 2
    2 2
5
    1 1 1 1 1
    2 1 1 1
    1 2 1 1
    1 1 2 1
    1 1 1 2
    2 2 1
    2 1 2
    1 2 2

4를 기준으로 보면
2를 1개도 사용하지 않고 구할 수 있는 수: 1
2를 1개만 사용하고 구할 수 있는 수: 3
2를 2개만 사용하고 구할 수 있는 수: 1
로 이를 수식으로 표현하면
4C0 + 3C1 + 2C2 가 된다.
즉, sum(n-iCi), n - i >= i  이 성립된다.

5를 해당 공식에 대입하면,
5C0 + 4C1 + 3C2 = 8 이다.
물론 피보나치보단 느리다.
"""


def solution(n):
    def fib(n):
        curr, _next = 0, 1
        for _ in range(n):
            curr, _next = _next, curr + _next
        return curr

    return fib(n+1) % 1234567


import operator as op
from functools import reduce


def solution1(n):
    def nCr(n, r):
        r = min(r, n - r)
        numerator = reduce(op.mul, range(n, n - r, -1), 1)
        denominator = reduce(op.mul, range(1, r + 1), 1)
        return numerator // denominator

    answer = 0
    i = 0
    while n - i >= i:
        answer += nCr(n - i, i)
        i += 1

    return answer % 1234567


assert solution(4) == 5
assert solution(3) == 3
