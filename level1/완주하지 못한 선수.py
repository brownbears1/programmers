"""
중복 키가 존재하므로 set()은 사용못함
"""


# def solution(participant, completion):
#     """
#     아무래도 복잡도가 completion의 개수 * parcipant의 개수 m 으로 O(n) * O((n-1))로 n 제곱이 나와 시간초과
#     """
#     for person in completion:
#         participant.remove(person)
#
#     return participant[0]


# def solution(participant, completion):
#     """
#     # 테스트 1 〉	통과 (28.97ms, 21.7MB)
#     # 테스트 2 〉	통과 (44.81ms, 25.2MB)
#     # 테스트 3 〉	통과 (56.57ms, 27.5MB)
#     # 테스트 4 〉	통과 (67.27ms, 34MB)
#     # 테스트 5 〉	통과 (60.72ms, 34MB)
#     내장함수 사용하지 않고 구현한 버
#     """
#     participant_dict = {}
#     for p in participant:전
#         if not participant_dict.get(p):
#             participant_dict[p] = 1
#         else:
#             participant_dict[p] += 1
#
#     for c in completion:
#         participant_dict[c] -= 1
#         if not participant_dict[c]:
#             participant_dict.pop(c)
#
#     return participant_dict.popitem()[0]


# import collections
#
#
# def solution(participant, completion):
#     """
#     collections의 Counter함수를 사용해서 구현한 버전
#     Counter 함수는 iterable한 타입의 데이터를 키: 반복횟수 로 저장한다.
#     또한 Counter() - Counter()가 내부적으로 계산이 되는데 좌변 기준으로 우변에 키가 있을 경우 연산을 하고, 좌변 <= 우변 일 경우, 결과에서 삭제한다.
#
#     """
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return answer.popitem()[0]


from itertools import zip_longest
from collections import defaultdict


def solution(participant, completion):
    """
    # 테스트 1 〉	통과 (32.78ms, 21.7MB)
    # 테스트 2 〉	통과 (44.76ms, 25.2MB)
    # 테스트 3 〉	통과 (60.33ms, 27.6MB)
    # 테스트 4 〉	통과 (65.73ms, 33.9MB)
    # 테스트 5 〉	통과 (60.30ms, 34MB)
    """
    result = defaultdict(int)
    for p, c in zip_longest(participant, completion):
        result[p] += 1
        result[c] -= 1

    # sort 함수는 n * log(n) 이라서 반복문 1번 도는 것보다 비용이 크다.
    # return sorted(result.items(), key=lambda k:k[1])[-1][0]

    for key in result:
        if result[key] > 0:
            return key


assert solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']) == 'leo'
assert solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']) == 'vinko'
assert solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']) == 'mislav'
