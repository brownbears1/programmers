"""
연산자 우선순위에 등호는 없음
연산자가 n개가 주어진다면 조합의 최대 가지수는 n!임
계산 결과가 음수값이면 절대값으로 표현
연산자는 +,-,* 3개만 주어짐
피연산자는 0이상 999 이하의 수
- 피연산자가 음수는 들어오지 않음
표현식은 최소 1개의 연산자가 존재
최종(중간) 결과의 값은 2^63 - 1 이하의 수
같은 연산자끼리는 앞에 나온 것이 우선순위가 더 높음


우선순위가 높은 애들을 분리 시킨 후, 전부 분리가 됐다면 eval을 통해 계산을 한다.
즉, 계산이 되는 순서는 우선 순위가 낮은 애들부터 계산이 된다.
어차피 연산자 우선순위가 (+, -), (-, +)과 같이 순서만 바뀐 쌍이 있기 때문에 가능하다.
"""

from itertools import permutations


def solution(expression):
    def calc(n, e):
        if n == 2:
            return str(eval(e))
        return str(eval(priority[n].join([calc(n + 1, element) for element in e.split(priority[n])])))

    answer = 0
    for priority in permutations('+-*', 3):
        res = int(calc(0, expression))
        answer = max(answer, abs(res))

    return answer


# def solution(expression):
#     """
#     다른 사람이 통과한 답인데 간단(깔끔)하게 해결한 것 같아서 퍼옴
#     """
#     operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
#     answer = []
#     for op in operations:
#         a = op[0]
#         b = op[1]
#         temp_list = []
#         for e in expression.split(a):
#             temp = [f"({i})" for i in e.split(b)]
#             temp_list.append(f'({b.join(temp)})')
#         answer.append(abs(eval(a.join(temp_list))))
#     return max(answer)


assert solution("100-200*300-500+20") == 60420
assert solution("50*6-3*2") == 300
