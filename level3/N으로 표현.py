"""
1 = 1
2 = 1 + 1
3 = 1 + 2 = 2 + 1
4 = 1 + 3 = 2 + 2 = 3 + 1
5 = 1 + 4 = 2 + 3 = 3 + 2 = 4 + 1

위 공식처럼 이전에 계산한 결과값들을 조합해 8번까지 진행하고 그 안에 구하고자 하는 수가 없는 경우, -1을 반환하면 된다.
문제의 5를 가지고 예시를 들어보자

1개사용:
    5
2개 사용:
    5 + 5
    5 - 5
    5 / 5
    5 + 5
    55
3개 사용:
1개 사용 + 2개 사용
    5 + (5 + 5)
    5 - (5 + 5)
    5 / (5 + 5)
    5 * (5 + 5)

    5 + (5 - 5)
    5 - (5 - 5)
    5 / (5 - 5)
    5 * (5 - 5)

    5 + (5 / 5)
    5 - (5 / 5)
    5 / (5 / 5)
    5 * (5 / 5)

    5 + (5 * 5)
    5 - (5 * 5)
    5 / (5 * 5)
    5 * (5 * 5)

    5 + 55
    5 - 55
    5 / 55
    5 * 55
2개 사용 + 1개 사용
    (5 + 5) + 5
    (5 + 5) - 5
    (5 + 5) / 5
    (5 + 5) * 5

    (5 - 5) + 5
    (5 - 5) - 5
    (5 - 5) / 5
    (5 - 5) * 5

    (5 / 5) + 5
    (5 / 5) - 5
    (5 / 5) / 5
    (5 / 5) * 5

    (5 * 5) + 5
    (5 * 5) - 5
    (5 * 5) / 5
    (5 * 5) * 5

    55 + 5
    55 - 5
    55 / 5
    55 * 5

와 같이 이전에 계산한 값들을 그대로 사용하는 것을 볼 수 있다. 여기서 나온 계산 결과가 동일하다면 중복 제거를 통해 연산량을 줄일 수 있다.
"""


def solution(N, number):
    if N == number:
        return 1
    partial_result = [{N}]

    for i in range(2, 9):
        partial_set = set()
        for j in range(1, i):
            for l in partial_result[j - 1]:
                for r in partial_result[i - j - 1]:
                    partial_set.add(l + r)
                    partial_set.add(l - r)
                    partial_set.add(l * r)
                    if r:
                        partial_set.add(l // r)

        partial_set.add(int(str(N) * i))
        if number in partial_set:
            return i
        partial_result.append(partial_set)
    return -1


assert solution(5, 12) == 4
assert solution(2, 11) == 3
assert solution(5, 5) == 1
