"""
문제를 잘 읽으면 여벌의 체육복을 가져온 학생도 도난 당할 수 있음
그럴 때, 여벌 = 도난 이 성립되어 다른 학생에게 나눠줄 수 없음

우선순위
1. 내 체육복 상태
2. 도난 당한 내 뒤의 학생
3. 도난 당한 내 앞의 학생


제일 먼저 도난 당한 학생과 여벌 옷을 가져온 학생 사이에서 둘 다 속한 (여벌옷 가져왔는데 도난 당한 학생) 학생들을 제거해준다.
그러면 위 우선순위에서 1번을 고려할 필요가 사라지므로 코드가 간결해진다.
다음 우선순위에 따라 여벌옷이 있으면 도난 당한 내 뒤의 학생이 있는지, 내 앞의 학생이 있는지 찾아 없애주면 된다.
"""


def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    lost_set.difference_update(set(reserve))
    reserve_set.difference_update(set(lost))

    for student in range(1, n+1):
        if student in reserve_set:
            if student - 1 in lost_set:
                lost_set.remove(student - 1)
                continue

            if student + 1 in lost_set:
                lost_set.remove(student + 1)

    return n - len(lost_set)


assert solution(5, [2, 4], [1, 3, 5]) == 5
assert solution(5, [2, 4], [3]) == 4
assert solution(3, [3], [1]) == 2
assert solution(7, [2, 3, 4], [1, 2, 3, 6]) == 6
