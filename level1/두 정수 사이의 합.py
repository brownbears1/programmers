def solution(a, b):
    return sum(range(b, a+1) if a > b else range(a, b+1))


assert solution(3, 5) == 12
assert solution(3, 3) == 3
assert solution(5, 3) == 12
