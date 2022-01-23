"""

문제가 생각보다 간단했다.
소수인지 판별하는 수를 구하는 방식은 총 4가지이다.
0P0, P0, 0P, P(0을 포함하지 않음)

전부 0와 근접해야 하므로 0으로 쪼개버리고 ''와 1을 제외한 수들을 소수인지 판별하면 되는 문제이다.
"""

import math
import string


def numeral_system(number, base):
    q, r = divmod(number, base)
    n = string.digits[r]
    return numeral_system(q, base) + n if q else n


def is_prime(n):
    max_length = int(math.sqrt(n)) + 1

    for i in range(2, max_length):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    count = 0
    value = numeral_system(n, k)
    targets = str(value).split('0')

    for target in targets:
        if not target or target == '1':
            continue

        if is_prime(int(target)):
            count += 1
    return count


assert solution(437674, 3) == 3
assert solution(110011, 10) == 2
