def solution(numbers):
    return sum({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(set(numbers)))


assert solution([1,2,3,4,6,7,8,0]) == 14
assert solution([5,8,4,0,6,7,9]) == 6
