def solution(arr):
    target = arr.pop(0)
    result = [target]

    for a in arr:
        if target != a:
            result.append(a)
            target = a

    return result


assert solution([1,1,3,3,0,1,1]) == [1,3,0,1]
assert solution([4,4,4,3,3]) == [4,3]
