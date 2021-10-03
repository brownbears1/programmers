"""
만나게 하는 모든 방법이 and 조건이여야지만 가능

1) 입실명부 순서와 퇴실명부 순서가 반드시 반대여야함
2) 입실명부 또는 퇴실명부 둘 중 인접해야 한다 (이건 아닌듯)


로직세워서 하기가 생각보다 껄끄러워서 임시 큐를 두고 insert/delete 방식으로 진행했다.
psuedo 순서는 다음과 같다.
1. 임시 큐에 데이터 삽입
2. 임시 큐의 길이가 2 이상이면 만나는 데이터들을 +1
3. 퇴실 순서에 맞게 삭제
4. 1~3번을 반복
"""

from collections import deque


def solution(enter, leave):
    answer = [0] * len(enter)
    leave = deque(leave)
    temp_queue = []

    for num in enter:
        for queue_num in temp_queue:
            answer[queue_num-1] += 1
            answer[num-1] += 1

        temp_queue.append(num)

        while leave and leave[0] in temp_queue:
            temp_queue.remove(leave[0])
            leave.popleft()

    return answer


assert solution([1, 3, 2], [1, 2, 3]) == [0, 1, 1]
assert solution([1, 4, 2, 3], [2, 1, 3, 4]) == [2, 2, 1, 3]
assert solution([3, 2, 1], [2, 1, 3]) == [1, 1, 2]
assert solution([3, 2, 1], [1, 3, 2]) == [2, 2, 2]
assert solution([1, 4, 2, 3], [2, 1, 4, 3]) == [2, 2, 0, 2]
