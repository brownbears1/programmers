"""
팰린드롬은 뒤집어도 동일한 문자열을 뜻한다.
예) 기러기, 토마토, wow

주어진 문자열을 dictionary화 하여 위치 값을 리스트로 저장하고 해당 위치값 리스트를 순회하면서 비교해나간다.
비교하기 전에 이전 최대 팰린드롬의 길이보다 비교할 값이 적다면 비교를 하지 않는다. (최대 길이를 구하는 문제이므로 팰린드롬이라 해도 계산을 할 필요가 없다.)

아래 풀이는 효율성 1번이 1400ms정도 나온다. 더 빠르게 하는 방법은 모르겠다.

+
반복문 세번째에서 앞에서부터 실행하는 것이 아닌, 뒤에서부터 실행하도록 하면 효율성 1번을 제외하고 속도를 줄일 수 있다.
- 0번째와 n번째의 문자열이 팰린드롬인지 비교를 하고 만약 팰린드롬이라면 n-1번째를 비교할 필요가 없기 때문이다.
- 미리 조합을 진행하고 1번째 - 0번째 + 1로 정렬을 처리하고 반복문만 돌려서 처리하면 속도를 줄일 수 있을 것 같다.

"""
from collections import defaultdict


def solution(s):
    answer = 1
    char_dict = defaultdict(list)

    for i, c in enumerate(s):
        char_dict[c].append(i)

    for _, value in char_dict.items():
        for i in range(len(value) - 1):
            for j in range(len(value)-1, i, -1):
                target = s[value[i]: value[j] + 1]
                length = value[j] - value[i] + 1

                if answer >= length:
                    break

                if target == target[::-1]:
                    answer = length

    return answer


# from collections import defaultdict
# from itertools import combinations
#
#
# def solution(s):
#     """
#     더 오래 걸리네
#     """
#     answer = 1
#     char_dict = defaultdict(list)
#
#     for i, c in enumerate(s):
#         char_dict[c].append(i)
#
#     _list = []
#     for _, value in char_dict.items():
#         _list.extend(combinations(value, 2))
#
#     _list.sort(key=lambda x: x[1] - x[0], reverse=True)
#
#     for i, j in _list:
#         target = s[i: j + 1]
#         length = j - i + 1
#
#         if answer >= length:
#             continue
#
#         if target == target[::-1]:
#             answer = length
#
#     return answer

assert solution('abcdcba') == 7
assert solution('abacde') == 3
assert solution('ecdabbeadc') == 2
assert solution('a') == 1
assert solution('abaabaaaaaaa') == 7