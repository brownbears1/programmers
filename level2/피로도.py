"""
최대 길이는 8이므로 조합을 만드는 최대 반복 수는 8!

길이가 길지 않으므로 완전탐색을 한다.
만약 길이가 길고 효율성도 채점을 한다면 bfs나 dfs로 풀어야 할 것 같다.

"""

from itertools import permutations


def solution(k, dungeons):
    max_cnt = 0
    dungeon_cnt = len(dungeons)
    for case in permutations(dungeons, dungeon_cnt):
        fatigue = k
        cnt = 0
        for minimum, consumption in case:
            if fatigue < minimum:
                break
            fatigue -= consumption
            cnt += 1

        max_cnt = max(max_cnt, cnt)
        if dungeon_cnt == max_cnt:
            break
    return max_cnt


assert solution(80, [[80, 20], [50, 40], [30, 10]]) == 3
