"""
약수 구하는 공식 가져와서 풀었는데 문제를 간단하게 해결할 수도 있었다.
약수는 무조건 쌍으로 나오므로 짝수인데 문제를 보면 4의 약수 1, 2, 4 와 같이 동일한 값일 경우,중복을 제거해야한다.

그러므로 주어진 수에 루트를 씌워 나머지가 없이 몫만 나오게 된다면 해당 값을 약수가 홀수가된다.
"""
import math


# def solution(left, right):
#     """
#     내 풀이
#     """
#     def get_divisor(num):
#         divisors = set()
#         length = int(math.sqrt(num)) + 1
#         for i in range(1, length):
#             if not num % i:
#                 divisors.add(i)
#                 divisors.add(num // i)
#         return divisors
#
#     answer = 0
#     for n in range(left, right + 1):
#         answer += n if not len(get_divisor(n)) % 2 else -n
#
#     return answer


def solution(left, right):
    """
    루트를 씌운 풀이
    """
    answer = 0
    for n in range(left, right + 1):
        answer += -n if math.sqrt(n).is_integer() else n
    return answer


assert solution(13, 17) == 43
assert solution(24, 27) == 52
