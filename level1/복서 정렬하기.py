"""
개노가다 문제
"""


def solution(weights, head2head):
    score_list = []
    # 승률, 자기보다 무거운 복서를 이긴 횟수, 자기 몸무게, 자기 순번
    for i, records in enumerate(head2head):
        score_list.append([0, 0, 0, 0])
        total_cnt = 0
        win_cnt = 0
        for j, record in enumerate(records):
            if record == 'N':
                continue
            elif record == 'W':
                win_cnt += 1
                if weights[i] < weights[j]:
                    score_list[i][1] += 1
            total_cnt += 1

        score_list[i][0] = 0 if not total_cnt else win_cnt / total_cnt
        score_list[i][2] = weights[i]
        score_list[i][3] = i + 1

    score_list.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    return list(map(lambda x: x[3], score_list))


assert solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]) == [3, 4, 1, 2]
assert solution([145, 92, 86], ["NLW", "WNL", "LWN"]) == [2, 3, 1]
assert solution([60, 70, 60], ["NNN", "NNN", "NNN"]) == [2, 1, 3]
