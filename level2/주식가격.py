"""
스택 맞나?
"""

from collections import deque


def solution(prices):
    def stock(target):
        for i, price in enumerate(prices):
            if target > price:
                return i + 1

        return len(prices)

    prices = deque(prices)
    results = []

    while prices:
        results.append(stock(prices.popleft()))

    return results


assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
