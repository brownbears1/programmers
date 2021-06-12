"""
탑-다운 방식으로 해결하면 모든 경우의 수를 다 진행하기 때문에 시간초과가 발생한다.
반대로 다운-탑 방식으로 진행하여 해결

1. 최대 높이, 최대 너비 만큼의 2차원 배열을 만든 후 0으로 초기화
2. 가장 바닥에서부터 시작하여 꼭대기로 올라가도록 반복문 진행
3. 부모에서 자식으로 갈 수 있는 방향은 왼쪽, 오른쪽 두가지만 존재하므로 max(현재값 + 2차원 배열[h+1][w], 현재값 + 2차원 배열[h+1][w+1)의 값 계산
4. 위에서 계산한 값이 2차원 배열의 값보다 클 경우, 교체

이렇게 하면 최종 결과는 2차원 배열[0][0]에 들어가 있다.
"""


# def solution(triangle):
#     """
#     시간초과
#     """
#     def dp(h, w, value):
#         if h == height:
#             answer.append(value)
#             return
#         value += triangle[h][w]
#         dp(h + 1, w, value)
#         dp(h + 1, w + 1, value)
#
#     answer = []
#     height = len(triangle)
#     dp(0, 0, 0)
#
#     return max(answer)


def solution(triangle):
    height = len(triangle)
    width = len(triangle[-1])
    matrix = [[0] * width for _ in range(height)]

    height -= 1

    for reversed_h, row in enumerate(reversed(triangle)):
        h = height - reversed_h
        for w, value in enumerate(row):
            if height != h:
                left = value + matrix[h + 1][w]
                right = value + matrix[h + 1][w + 1]
                value = max(left, right)

            if matrix[h][w] < value:
                matrix[h][w] = value

    return matrix[0][0]


assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30
