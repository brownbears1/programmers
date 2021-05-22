"""
먼저 1 ~ 최대값을 두고 (시작값 + 종료값) // 2 를 중간으로 두고 이 중간 값과 찾고자 하는 값이 같은지 비교하는 것이 이분검색이다.
이를 문제에 대입하면 중간값을 찾고 해당 중간값 / 심사관 처리 시간 을 하면 주어진 시간에 해당 심사관이 몇명을 심사할 수 있는지 알 수 있다.

또한 최소 시간을 찾는 것이므로 위 식에서 구한 값이 주어진 심사인원과 같거나 클 때마다 값을 저장한다.
이러한 방식을 start가 end보다 커질 때까지 반복한다.

재귀함수로 해보려고 했는데 문제가 껄끄러워져서 포기
"""


def solution(n, times):
    start = 1
    answer = end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        _sum = sum(mid // time for time in times)

        if n <= _sum:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


assert solution(6, [7, 10]) == 28
assert solution(2, [1, 2]) == 2
