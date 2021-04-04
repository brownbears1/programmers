"""
주어진 수의 순서는 변경할 수 없다.
len(number) - k 와 k 중 작은 수로 구하는 것이 효율적이다
- k 가 작을 경우, number에서 k개 만큼 제거
- len(number) - k 가 작을 경우, number 에서 len(number) - k 개 만큼 선택

combinations 함수를 사용하면 시간초과
- 테스트 3~10 시간초과 실패

Tip:
- 9의 경우 한 자리 수 중 가장 큰 수이므로 9가 나왔을 때, 바로 저장하고 다음으로 넘겨야 한다. (안그러면 시간초과가 발생한다)
- 최대값을 구할 때,주어진 수에 0이 존재할 수도 있어서 초기 최대값을 0으로 두면 안된다.

먼저 12번 케이스에서 막혀서 해결을 못했다.
풀이 컨셉은 다음과 같다.

1. 주어진 수 number가 4177252841 이고 k가 4라면 만들어야 하는 자리수는 6자리이다.
2. number에서 가장 첫 번째 자리수를 선택한다고 했을 때, 41772 에서 선택을 해야 한다.
-  순서가 보장되기 때문에 만약에 2를 선택한다고 하면 6자리를 만들기 위해 52841가 기본으로 따라온다.
3.  41772에서 3번째 자리를 선택하고 이제 만들어야 하는 자리수는 5자리이다.
4. 따라서 725 에서 두번째 자리에 들어갈 수를 구한다.
- 2번과 동일하게 순서가 보장되기 때문에 만약에 5를 선택한다고 하면 5자리를 만들기 위해 2841가 기본으로 따라온다.
5. 2~4번을 min(k, len(number) - k)번 반복한다.
- 범위를 지정하고 자리수를 앞에서부터 선택해 만드는 방식이므로 최소로 반복해야 한다.
6. 5번의 반복문이 끝나고 나온 결과값의 길이가 만들어야 할 자리수의 길이(len(number) - k)와 같지 않다면 4번에서 선택한 뒷자리들을 붙인다.



구글링 했을 때 12번 케이스가
assert solution('999', 1) == '99'
assert solution('111119', 3) == '119'
assert solution('10000', 1) == '1000'
assert solution("7777777", 2) == "77777"

통과하면 된다는데 통과하는데도 12번에서 튕긴다.. 모르겠다.
- number[:k+1] 하니까 12번이 그냥 통과한다.
그러면 number = 77777, k = 1이라고 하면 '77' 이여야 정답이라는건데 이해가 안된다.
- number[:-1]도 통과한다.
number = 77777 일 때, k와 상관없이 7777이라는 소리다.


"""


def solution(number, k):
    answer = ''
    start_index = 0
    end_index = k
    answer_size = len(number) - k
    range_size = min(k, answer_size)

    for _ in range(range_size):
        max_value = '-1'
        end_index += 1
        temp_max_index = 0

        for j, n in enumerate(number[start_index:end_index]):
            if n == '9' or max_value < n:
                max_value = n
                temp_max_index = j + 1
                if n == '9':
                    break

        start_index += temp_max_index
        answer += max_value

    if len(answer) != answer_size:
        answer += number[end_index:]

    return answer


assert solution('1924', 2) == '94'
assert solution('1231234', 3) == '3234'
assert solution('4177252841', 4) == '775841'
assert solution('999', 1) == '99'
assert solution('111119', 3) == '119'
assert solution('10000', 1) == '1000'
assert solution("7777777", 2) == "77777"
assert solution("01010", 3) == "11"
assert solution('77777', 1) == '7777'
assert solution('11', 1) == '1'
assert solution('9999999', 1) == '999999'
