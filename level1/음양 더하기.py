"""
1줄로 풀면 멋있어보이긴 한데 list 변수가 불필요하게 생긴다.
"""


def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if not sign:
            absolute *= -1
        answer += absolute

    return answer


def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))


assert solution([4,7,12], [True,False,True]) == 9
assert solution([1,2,3], [False,False,True]) == 0
