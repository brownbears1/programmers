"""
도착지점의 대각선으로 웅덩이가 있으면 도착할 수가 없으므로 0을 리턴해야함
재귀로 풀면 무조건 시간초과 발생

방향이 오른쪽, 아래 두가지로 고정되어 있어 아래의 기법을 적용할 수 있다. (최소 이동 경로를 찾을 필요도 없다. 어차피 2가지로만 움직여야되니 불필요한 이동 경로가 발생하지 않기 때문이다.)
(0, 1), (0, 2), (0, n)을 이동할 수 있는 경우의 수는 1개
(1, 0), (2, 0), (n, 0)을 이동할 수 있는 경우의 수는 1개

(1, 1)을 이동할 수 있는 경우의 수는 (0, 1) + (1, 0) 의 합이다.
(1, 2)을 이동할 수 있는 경우의 수는 (0, 2) + (1, 1) 의 합이다.
즉, (m, n)을 이동할 수 있는 경우의 수는 (m-1, n) + (m, n-1) 의 합이다.

여기서 웅덩이는 지나갈 수 없으므로 0이라 고정해놓는다.
또한 y = 0이거나 x = 0일 때, 웅덩이가 존재하면 그 뒤로 지나갈 수 없으므로 0으로 초기화 해준다.
즉,
(0, 1)이 웅덩이라면 (0, 2), (0, 3), (0, n)은 지나갈 수 없으므로 0으로 초기화한다.
(2, 0)이 웅덩이라면 (3, 0), (4, 0), (n, 0)은 지나갈 수 없으므로 0으로 초기화한다.


마지막으로  1000000007의 나머지로 출력하라 하는데 이는 결과를 반환할 때 해줘도 되지만 중간 결과 값이 너무 클 경우(int 범위를 넘을 경우) 도중 에러가 날 수 있으므로
중간 계산식에서 1000000007의 나머지를 더하도록 처리한다.
어차피 (a + b) % c = a % c + b % c 와 같이 중간에 하나 마지막에 하나 결과는 같기 때문이다.
"""

# def solution(m, n, puddles):
#     """
#     재귀로 모든 칸을 움직이는 방식으로 하면 정답은 맞지만 시간초과가 무조건 발생한다.
#     """
#     # 출발지에 웅덩이가 오른쪽, 아래로 있거나 도착지 기준으로 왼쪽이나 위에 있으면 0 반환
#     if ([m-1, n] in puddles and [m, n-1] in puddles) or ([1,2] in puddles and [2,1] in puddles):
#         return 0
#
#     answer = 0
#
#     def go(y, x):
#         nonlocal answer
#         if x == m or y == n:
#             return
#
#         if not matrix[y][x]:
#             return
#
#         if x == m - 1 and y == n - 1:
#             answer += 1
#             answer %= 1000000007
#             return
#
#         go(y, x+1)
#         go(y+1, x)
#
#     matrix = [[True] * m for _ in range(n)]
#     for puddle in puddles:
#         matrix[puddle[1] - 1][puddle[0] - 1] = False
#
#     go(0, 0)
#     return answer % 1000000007


def solution(m, n, puddles):
    matrix = [[1] * m for _ in range(n)]

    for puddle in puddles:
        y = puddle[1] - 1
        x = puddle[0] - 1
        matrix[y][x] = 0

        if not y:
            matrix[0][x:] = [0] * m

        if not x:
            for j in range(y, n):
                matrix[j][0] = 0

    for y, row in enumerate(matrix):
        if not y:
            continue
        for x, value in enumerate(row):
            if not (value and x):
                continue

            matrix[y][x] = (matrix[y - 1][x] + matrix[y][x - 1]) % 1000000007

    return matrix[-1][-1]


assert solution(4, 3, [[2, 2]]) == 4
