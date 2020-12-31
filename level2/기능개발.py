import math


# def solution(progresses, speeds):
#     left_days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
#
#     result = [0]
#     target = left_days[0]
#
#     for day in left_days:
#         if target >= day:
#             result[-1] += 1
#         else:
#             target = day
#             result.append(1)
#
#     return result


def solution(progresses, speeds):
    result = []
    target = 0
    for p, s in zip(progresses, speeds):
        left_day = math.ceil((100 - p) / s)
        if target >= left_day:
            result[-1] += 1
        else:
            target = left_day
            result.append(1)

    return result


assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
