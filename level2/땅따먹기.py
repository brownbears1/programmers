"""
탐욕법으로 첫 선택할 수 있는 가장 큰 값을 선택하면서 내려가기 (X)
해당 문제는 탐욕법이 아니라 DP 문제임
DP는 항상 결과가 최대 또는 최소값이여야 한다.
최대 시간 복잡도는 4x3^9999 이므로 재귀로는 불가능해보인다.


i=0) 1, 2, 3, 5
i=1) 5, 6, 7, 8

이라 할 때, i=1, j=0의 가장 최대값을 구하는 방법은 i=0에서 j=0을 제외한 j=1,2,3의 최대값을 더하면 된다.
i=0에서 j=0을 제외한 이유는 같은 열을 밟을 수 없는 규칙 때문이다.
즉, land[1][0] += max(land[0][1], land[0][2], land[0][3]) 이다.

위와 같은 방법으로 전부 구해보면 다음과 같은 로직이 나온다.
land[1][0] += max(land[0][1], land[0][2], land[0][3])
land[1][1] += max(land[0][0], land[0][2], land[0][3])
land[1][2] += max(land[0][0], land[0][1], land[0][3])
land[1][3] += max(land[0][0], land[0][1], land[0][2])

위 로직에 숫자를 대입하면
5 += max(2, 3, 5) = 5+5 = 10
6 += max(1, 3, 5) = 6+5 = 11
7 += max(1, 2, 5) = 7+5 = 12
8 += max(1, 2, 3) = 8+3 = 11

여기서 최고점을 구하면 되므로 12가 된다.


위 로직을 그대로 예제에 대입하면
0)
1, 2, 3, 5
5, 6, 7, 8
4, 3, 2, 1

1)
10, 11, 12, 11
 4,  3,  2, 1

2)
16, 15, 13, 13

= 16 이 된다.

과거의 결과를 그대로 사용하므로 DP 풀이법이다.
"""


def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
    return max(land[-1])


assert solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]) == 16
assert solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]) == 20
