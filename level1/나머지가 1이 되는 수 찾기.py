def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i


assert solution(10) == 3
assert solution(12) == 11
