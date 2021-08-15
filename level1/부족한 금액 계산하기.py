"""
그냥 등차수열의 합을 대입하면 되긴한다.
price * (1+2+3+...+n)이길래 아래와 같이 처리하고
위 식의 결과 - money를 해서 양수이면 해당 값을 반환하고 0이거나 음수이면 돈이 모자르지 않으니 지문에서 출력하라고 하는 0을 출력하면 된다.
"""


def solution(price, money, count):
    return max(0, price * sum(range(count + 1)) - money)


assert solution(3, 20, 4) == 10
