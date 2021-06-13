from collections import defaultdict


def solution(genres, plays):
    answer = []
    _dict = defaultdict(list)
    _sum = defaultdict(int)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        _dict[genre].append([i, play])
        _sum[genre] += play

    _ordering = sorted(_sum.items(), key=lambda x: -x[1])

    for genre, _ in _ordering:
        for index, _ in sorted(_dict[genre], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(index)

    return answer


assert solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]
