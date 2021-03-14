"""
가장 많이.
"""

from itertools import combinations
from collections import Counter


# def solution(orders, course):
#     """
#     13, 14 시간초과
#     반복문이 3개가 중첩돼서 그런듯
#     """
#     s = defaultdict(set)
#     answer = []
#     # 메뉴 별 주문한 사람들을 나열
#     for i, set_order in enumerate(orders):
#         for order in set_order:
#             s[order].add(i+1)
#
#     for num in course:
#         temp_dict = defaultdict(list)
#         for menu in combinations(s, num):
#             temp = set()
#             for i, people in enumerate(menu):
#                 if not i:
#                     temp = temp | s[people]
#                 else:
#                     temp = temp & s[people]
#
#             temp_dict[len(temp)].append(''.join(sorted(menu)))
#
#         max_course = max(temp_dict)
#
#         if max_course < 2:
#             continue
#         answer.extend(temp_dict[max_course])
#         answer.sort()
#     return answer

def solution(orders, course):
    """
    들어온 주문을 요구되는 course로 조합 형태를 만들고 이를 Counter 함수를 사용해 개수 파악
    """
    answer = []
    for demanded_course in course:
        order_combination = Counter()
        for order in orders:
            order_combination.update(map(lambda x: ''.join(x), combinations(sorted(order), demanded_course)))

        most_common_list = order_combination.most_common()
        if not most_common_list:
            continue

        max_num = most_common_list[0][1]
        if max_num < 2:
            continue

        answer.extend(order[0] for order in most_common_list if order[1] == max_num)

    return sorted(answer)


assert solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"]
assert solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"]
assert solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"]
