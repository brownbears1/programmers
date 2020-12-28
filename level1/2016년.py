import datetime


def solution(a, b):
    weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return weeks[datetime.date(2016,a, b).weekday()]


# def solution(a, b):
#     weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     thirtyone = [1, 3, 5, 7, 8, 10, 12]
#     thirty = [4, 6, 9, 11]
#
#     for month in range(1, a):
#         if month in thirtyone:
#             b += 31
#         elif month in thirty:
#             b += 30
#         else:
#             b += 29
#
#     return weeks[(b - 1) % len(weeks)]


assert solution(5, 24) == 'TUE'
