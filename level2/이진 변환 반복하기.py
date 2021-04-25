"""
순서는 다음과 같다.
1. 0의 개수 세기
2. 0을 빈값으로 변경
3. 2번의 처리가 된 변수의 길이 계산
4.  길이를 2진수로 변경
5. 값이 1만 존재할 때까지 1~4번 반복

여기서 format 함수를 사용하면 bin 함수를 사용한 다음, 2진수를 나타내는 0b를 제거하는 방식을 하지 않아도 된다.
- format(값, '#b') 하면 0b101010 과 같이 나오고 #을 제거하고 'b'만 하면 101010만 추출
"""


def solution(s):
    answer = [0, 0]

    while s != '1':
        answer[1] += s.count('0')
        answer[0] += 1
        s = format(len(s.replace('0', '')), 'b')

    return answer


assert solution("110010101001") == [3, 8]
assert solution("01110") == [3, 3]
assert solution("1111111") == [4, 1]



