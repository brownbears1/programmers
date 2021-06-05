"""
문제에 함정이 있다.
[0, 3] 이면 0ms 부터 시작하는데 만약 [1, 3] 이면 1ms 부터 시작해 총 4ms라 생각했지만 첫 디스크가 들어오기 전까지 흐른 시간은 계산하지 않아야 한다.
즉, [[1, 3]] 가 있으면 총 소요 시간은 4ms 가 아닌 3ms다. ([[0, 3]]과 동일


heapq와 deque를 사용해 가장 큰 수를 heap 정렬한 다음, deque.popleft()로 꺼내서 쓰면 될 거 같은데 이중 어레이를 어떻게 heapq에 적용시킬 지 모르겠다.
그래서 비효율이 존재하지만
리스트 내 가능한 디스크 모두 검색 -> 존재하면 가능한 디스크들 중 가장 작은 디스크 선택 -> 해당 디스크 삭제 -> 시간계산

과 같은 방법으로 해결했다.

다른 풀이를 보니 heap보다 약 10배 이상 속도 차이가 난다.
"""


def solution(jobs):
    jobs.sort(key=lambda x: x[0], reverse=True)

    _sum = 0
    total_time = 0
    cnt = len(jobs)

    while jobs:
        _filter_jobs = list(filter(lambda x: x[0] <= total_time, jobs))
        if _filter_jobs:
            min_data = min(_filter_jobs, key=lambda x: x[1])
            jobs.remove(min_data)

            start_time, required_time = min_data
            if not _sum:
                _sum = required_time
            else:
                _sum += total_time + required_time - start_time
            total_time += required_time
        else:
            total_time += 1
    return _sum // cnt


assert solution([[0, 3], [1, 9], [2, 6]]) == 9
assert solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]) == 13
assert solution([[1, 9], [0, 11]]) == 15
assert solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]) == 13
assert solution([[0, 3], [0, 1], [4, 7]]) == 4
assert solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]) == 13
