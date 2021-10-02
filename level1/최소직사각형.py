"""
ez
"""


def solution(sizes):
    max_left = 0
    max_right = 0

    for _size in sizes:
        left, right = sorted(_size)
        max_left = max(left, max_left)
        max_right = max(right, max_right)

    return max_left * max_right


assert solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000
assert solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120
assert solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133
