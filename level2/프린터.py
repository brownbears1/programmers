"""
pop(0)의 복잡도는 O(N)
- 0번째 인덱스를 지우고 리스트 n-1개를 전부 앞으로 한 칸씩 땡기기 때문

복잡도를 줄이기 위해선 collections 모듈의 deque를 사용해야 한다. (pop(), popleft() 복잡도 O(1))
"""

from collections import deque


def solution(priorities, location):
    result = 0
    # O(n)
    custom = deque((p, i) for i, p in enumerate(priorities))
    # O(nlogn)
    max_value = sorted(priorities, reverse=True)
    
    while True:
        if custom[0][0] < max_value[result]:
            custom.append(custom.popleft())
        else:
            result += 1
            if custom.popleft()[1] == location:
                break

    return result


assert solution([2, 1, 3, 2], 2) == 1
assert solution([1, 1, 9, 1, 1, 1], 0) == 5
