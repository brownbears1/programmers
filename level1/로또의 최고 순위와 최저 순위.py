def solution(lottos, win_nums):
    if lottos.count(0) == 6:
        return [1, 6]

    ranking = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }

    cnt = 0
    for number in lottos:
        if number:
            cnt += win_nums.count(number)

    zero_cnt = lottos.count(0)

    return [ranking[cnt+zero_cnt], ranking[cnt]]


assert solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
assert solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6]
assert solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]
