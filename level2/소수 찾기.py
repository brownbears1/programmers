"""
에라토스테네스의 체를 사용해 소수를 구하면 된다.
설명: https://brownbears.tistory.com/445

기존 코드보다 다른 사람 풀이 중에 set을 사용해 더 단순하게 구하는 방식이 있어서 첨부함

"""
from itertools import permutations
import math


# def solution(numbers):
#     """
#     에라토스테네스의 체로 소수 목록을 구한 다음, 주어진 값이 소수인지 비교
#     """
#     def get_primes(n):
#         is_primes = [True] * n
#         max_length = math.ceil(math.sqrt(n))
#
#         for i in range(2, max_length):
#             if is_primes[i]:
#                 for j in range(i + i, n, i):
#                     is_primes[j] = False
#
#         return [i for i in range(2, n) if is_primes[i]]
#
#     permutations_result = []
#     cnt = 0
#
#     for i in range(len(numbers)):
#         permutations_result.extend(list(permutations(numbers, (i+1))))
#
#     all_numbers = list({int(''.join(number)) for number in permutations_result})
#     primes = get_primes(max(all_numbers) + 1)
#
#     for number in all_numbers:
#         if number in primes:
#             cnt += 1
#
#     return cnt


def solution(numbers):
    """
    내가 푼 방식보다 훨씬 깔끔함.
    set의 중복 요소 제거를 활요해 소수 목록을 구하는 식에서 역으로 소수가 아닌 리스트를 뽑은 다음, 주어진 값이 소수가 아니면 바로 지워나감
    """
    results = set()
    for i in range(len(numbers)):
        results.update(set(map(int, map(''.join, permutations(numbers, i+1)))))

    results = results.difference({0, 1})
    max_num = max(results)

    for i in range(2, math.ceil(math.sqrt(max_num))):
        results = results.difference(set(range(i * 2, max_num + 1, i)))

    return len(results)


assert solution('17') == 3
assert solution('011') == 2
