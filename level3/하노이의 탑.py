"""
원판 기둥은 무조건 3개
첫 번째 원판에서 세 번째 원판으로 최소로 옮겨야 한다.

하노이의 탑 최소 이동 횟수는 2^n - 1

15 이하의 자연수래서 재귀함수를 일반 반복문으로 풀려고 했는데 그냥 재귀도 통과하네
"""


def solution(n):
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n - 1, start, via, end)
            answer.append([start, end])
            hanoi(n - 1, via, end, start)

    answer = []
    hanoi(n, 1, 3, 2)

    return answer


assert solution(2) == [[1, 2], [1, 3], [2, 3]]
