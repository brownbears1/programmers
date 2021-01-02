"""
압축이 안된 문자는 1이라고 숫자를 붙이지 않음
길이를 계산할 땐 압축된 수까지 포함
압축조건은 무조건 첫 번째 문자부터 시작해야 된다.
전체 길이의 반 이상이 압축 조건으로 될 경우, 압축을 진행할 수 없으므로 반복문 실행할 때, 주어진 문자열 길이 / 2 만큼 실행하는 것이 속도를 줄일 수 있다.

비교를 진행할 때도, 기준이 되는 문자열 을 제외하고
"""


def solution(s):
    def compress(compression_index):
        standard = s[:compression_index]
        cnt = 0
        result = []
        compression = lambda x, y: f"{'' if not x else x + 1}{y}"

        for j in range(compression_index, length, compression_index):
            target = s[j:j + compression_index]

            if standard != target:
                result.append(compression(cnt, standard))
                standard = target
                cnt = 0
                continue

            cnt += 1
        result.append(compression(cnt, standard))

        return len(''.join(result))

    length = len(s)
    answer = 1000

    for i in range(0, length // 2 + 1):
        result = compress(i + 1)
        if result < answer:
            answer = result

    return answer


assert solution('a') == 1
assert solution('aaaaaaaaaaa') == 3
assert solution('aabbaccc') == 7
assert solution('ababcdcdababcdcd') == 9
assert solution('abcabcdede') == 8
assert solution('abcabcabcabcdededededede') == 14
assert solution('xababcdcdababcdcd') == 17
