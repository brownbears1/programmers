"""
dp문제임

2차원 배열로 진행했는데 다른 사람 풀이를 보니 1차원 배열로 간단하게 해결이 가능했다.
j번째의 경우의 수를 구하려면 m[i-1][j] + m[i][j - 거스름돈]이 된다.
"""


def solution(n, money):
    money.sort()

    matrix = [[1] + [0] * n for _ in range(len(money))]

    for i, m in enumerate(money):
        for change in range(1, n + 1):
            if not i:
                if not change % m:
                    matrix[i][change] = 1
                    continue

            if change < m:
                matrix[i][change] = matrix[i - 1][change]
                continue

            matrix[i][change] = (matrix[i - 1][change] + matrix[i][change - m]) % 1000000007

    return matrix[-1][-1]


# def solution(n, money):
#     """
#     1차원 배열로 푼 방식.
#     2차원 배열로 푼 것보다 훨씬 간단하고 보기 쉽다.
#     """
#     dp = [1] + [0] * n
#
#     for coin in money:
#         for price in range(coin, n+1):
#             if price - coin >= 0:
#                 dp[price] += dp[price-coin]
#     return dp[n] % 1000000007


assert solution(5, [1, 2, 5]) == 4
assert solution(10, [2, 3, 5, 7]) == 5
