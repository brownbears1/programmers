def solution(arr, divisor):
    return sorted([a for a in arr if not a % divisor]) or [-1]


assert solution([5, 9, 7, 10], 5) == [5, 10]
assert solution([2, 36, 1, 3], 1) == [1, 2, 3, 36]
assert solution([3,2,6], 10) == [-1]
