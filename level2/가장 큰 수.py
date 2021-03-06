"""
# 정수형 비교와 문자열 비교는 아래와 같다.
# 30 > 9 == True
# '30' > '9' == False
#
# 문자열의 경우, 맨 앞 문자부터 아스키코드로 변환이 되어 비교를 진행합니다.
# 따라서 위 '30' > '9' 의 경우, 먼저 '3'과 '9'를 아스키 코드로 변환해 비교를 진행하게 되는데 '9'의 아스키코드가 더 크므로 '30'의 마지막 '0'은 비교하지 않게 됩니다.
# - 아스키 코드 변환 비교
#     ord('3') > 'ord('9')
#
#
# sort(), sorted()에 빠져있지 말자
# 40, 403 의 경우에 40403 순으로 합치는 것이 40340보다 크다. 즉, 정렬을 할 때, a+b > b+a 와 같은 로직이 들어가야한다.

문제에서 원소의 크기는1000 이하라고 되어 있으니 최대 4자리의 숫자가 들어올 수 있다.
즉, 4자리 미만의 수를 전부 4자리로 만들어 버려서 비교를 하자
3, 30의 경우 [3, 30] 의 순서가 가장 큰 수이다. 따라서 4자리를 만들 때, 3000, 3000으로 하면 비교가 어려우므로 주어진 수를 반복해서 4자리를 만들어 버린다
3333 > 3030 이므로 정답이 된다.
"""

# def solution(numbers):
#     """
#     시간초과
#     """
#     numbers = list(map(str, numbers))
#     return str(max(list(map(int, (map(''.join, permutations(numbers, len(numbers))))))))


# def solution(numbers):
#     """
#     1. 주어진 수를 문자화 시켜 4번씩 반복한 다음, 4자리수까지만 자름
#     2. 첫 번쨰 열에 1번에서 구한 수, 두 번째엔 원래의 수를 넣음  [('6666', 6), ('1010', 10), ('2222', 2)]
#     3. 2번의 첫 번째 값으로 내림차순 정렬
#     4. 3번 결과 리스트에서 두 번째 데이터를 추출
#     5. 4번 결과 리스트를 문자열로 변환
#     6. 5번 결과를 정수로 변경
#     7. 6번 결과를 다시 문자열로 변경
#     """
#     return str(int(''.join(map(lambda x: str(x[1]), sorted([(int((str(num) * 4)[:4]), num) for num in numbers], key=lambda x: x[0], reverse=True)))))


def solution(numbers):
    """
    위에서 처럼 미리 구한 다음 계산하지 말고, 정렬 함수를 사용할 때, key에 람다를 사용해 직접 계산하도록 하는게 코드가 더 깔끔함
    """
    return str(int(''.join(sorted(map(str, numbers), key=lambda x: x * 4, reverse=True))))


assert solution([6, 10, 2]) == '6210'
assert solution([3, 30, 34, 5, 9]) == '9534330'
assert solution([40, 403]) == '40403'
assert solution([10, 101]) == '10110'
assert solution([1, 11, 111, 1111]) == '1111111111'
assert solution([0, 0, 0, 0, 0, 0]) == '0'
