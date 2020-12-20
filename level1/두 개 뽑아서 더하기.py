"""
파이썬에서의 set은 언뜻 보기엔 오름차순 순서를 보장하는 것 처럼 보이지만 사실은 hashset이기 때문에 오름차순 순서 보장이 되지 않는다.

import random
print(list(set(random.choices(range(1000), k=20))))

를 실행해보면
[960, 262, 423, 778, 619, 460, 717, 941, 591, 560, 337, 689, 305, 977, 407, 474, 283, 636, 894, 767]

와 같이 오름차순 으로 정렬이 되지 않는 것을 볼 수 있다.
"""


def solution(numbers):
    """
    기본형
    """
    answer = set()
    for i, n in enumerate(numbers):
        for m in numbers[i + 1:]:
            answer.add(n+m)
    return sorted(answer)


def solution1(numbers):
    """
    있어보이게 짠 형태
    """
    return sorted({n+m for i, n in enumerate(numbers) for m in numbers[i + 1:]})


from itertools import combinations


def solution2(number):
    """
    itertools의 combinations를 사용하기
    문제를 보면 조합을 구한 다음, 두 수를 더하고 오름차순으로 정렬하면 됨.
    combinations를 사용하면 조합을 쉽게 구할 수 있음.
    combinations로 2개 조합 구함 -> map을 사용해서 for 문을 줄임 -> set으로 중복 제거 -> sorted함수로 정렬
   """
    return sorted(set(map(lambda a: a[0]+a[1], combinations(number, 2))))


assert solution([2,1,3,4,1]) == [2,3,4,5,6,7]
assert solution([5,0,2,7]) == [2,5,7,9,12]
