"""
divmod로 아래 %, // 연산자를 대체할 수 있음
- 값이 작으면 divmod가 더 느리다고 함
"""

def solution(n):
    def ternary(v):
        if not v:
            return ''
        r = str(v % 3)
        v = v // 3
        return r + ternary(v)

    return int(ternary(n), 3)


assert solution(45) == 7
assert solution(125) == 229


# divmod 사용
def solution(n):
    def ternary(v):
        if not v:
            return ''
        v, r = divmod(v, 3)
        return str(r) + ternary(v)

    return int(ternary(n), 3)
