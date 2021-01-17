"""
접두사를 찾는 문제이므로 가장 첫 번째부터 맞는 개수가 있어야함
"""


def solution(phone_book):
    phone_book.sort()
    for i, phone in enumerate(phone_book):
        limit_index = len(phone)
        for target in phone_book[i + 1:]:
            if phone == target[:limit_index]:
                return False
    return True


# def solution(phone_book):
#     """
#     파이썬 내장함수 사용해서 푼 방법
#     """
#     phone_book.sort()
#
#     for i, phone in enumerate(phone_book):
#         if i+1 != len(phone_book) and phone_book[i+1].startswith(phone):
#             return False
#     return True


assert not solution(['119', '97674223', '1195524421'])
assert solution(['123', '456', '789'])
assert not solution(['12', '123', '1235', '567', '88'])
assert solution(['113', '44', '4544'])
assert not solution(['010111', '010'])
