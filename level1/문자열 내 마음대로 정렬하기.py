def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])


assert solution(['sun', 'bed', 'car'], 1) == ['car', 'bed', 'sun']
assert solution(['abce', 'abcd', 'cdx'], 2) == ['abcd', 'abce', 'cdx']
