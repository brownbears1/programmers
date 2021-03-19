"""
) 이게 먼저 나오거나 ( 이거의 개수보다 많아진다면 무조건 올바른 괄호가 될 수 없다.
"""


def solution(s):
    left = 0
    for bracket in s:
        if left < 0:
            break
        if bracket == ')':
            left -= 1
        else:
            left += 1

    return left == 0


assert solution("()()")
assert solution("(())()")
assert not solution(")()(")
assert not solution("(()(")
