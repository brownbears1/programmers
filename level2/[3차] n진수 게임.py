"""
생각나는 해결 방법은 2가지다.
n진법로 구한 수를 계속해서 더해나간 다음, p + m(미리구할숫자순서-1) 등차수열만큼 구하는 법과
n진법로 구한 수를 계속해서 비교해나가는 방식이다.

후자가 더 어려운거 같아 전자로 해결했다.
(물론 후자가 더 효율적이다)


아래 코드는 비효율적인 부분이 존재한다.

2진법, 사람 2명, 순서 1라고 가정하고 예를 들어, 2진법으로 나온 수가 11111111이면
1111 4개를 출력해야 하는데 아래 로직에서는 1만 추출하고 넘긴다.
"""


def solution(n, t, m, p):
    def numeral_system(number, base):
        q, r = divmod(number, base)
        n = NOTATION[r]
        return numeral_system(q, base) + n if q else n

    NOTATION = '0123456789ABCDEF'
    numeral = answer = ''
    i = 0
    ordering = p
    while len(answer) != t:
        numeral += numeral_system(i, n)
        target_index = ordering - 1
        i += 1
        # 튜브의 순서만큼 n진법의 수가 쌓일때까지 대기
        if len(numeral) <= target_index:
            continue
        answer += numeral[target_index]
        ordering += m
    return answer


assert solution(2, 4, 2, 1) == '0111'
assert solution(16, 16, 2, 1) == '02468ACE11111111'
assert solution(16, 16, 2, 2) == '13579BDF01234567'
