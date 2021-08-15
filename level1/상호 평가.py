"""
scores = list(map(list, zip(*scores)))
와 같이 미리 행열을 뒤집은 형태로 만들어서 구하는 계산식이 있지만
반복문을 중복으로 돌리기 싫어서 주어진 행렬을 그대로 사용함
"""


def solution(scores):
    def grade(avg):
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    answer = ''
    student_cnt = len(scores)

    for i in range(student_cnt):
        _sum = []
        denominator = student_cnt
        for j, score in enumerate(scores):
            _sum.append(score[i])

        if (_sum[i] == min(_sum) or _sum[i] == max(_sum)) and _sum.count(_sum[i]) == 1:
            _sum.pop(i)
            denominator -= 1

        answer += grade(sum(_sum) // denominator)

    return answer


assert solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]) == 'FBABD'
assert solution([[50,90],[50,87]]) == 'DA'
assert solution([[70,49,90],[68,50,38],[73,31,100]]) == 'CFD'
