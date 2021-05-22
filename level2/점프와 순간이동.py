"""
이진법으로 변경하면 1의 개수만큼 이동한다는 것을 알 수 있다.
"""
def solution(n):
    return format(n, 'b').count('1')


assert solution(5) == 2
assert solution(6) == 2
assert solution(5000) == 5
