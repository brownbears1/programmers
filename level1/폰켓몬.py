def solution(nums):
    # select_cnt = len(nums) // 2
    # total_cnt = len(set(nums))
    # return min(select_cnt, total_cnt)
    return min(len(nums) // 2, len(set(nums)))


assert solution([3, 1, 2, 3]) == 2
assert solution([3, 3, 3, 2, 2, 4]) == 3
assert solution([3, 3, 3, 2, 2, 2]) == 2
