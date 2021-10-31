"""

"""


def solution(n, left, right):
    start = left // n, left % n
    end = right // n, right % n
    arr = []

    for i in range(start[0], end[0]+1):
        element = 1 + i
        arr.extend([element] * element)
        arr.extend([j for j in range(element+1, n+1)])

    return arr[start[1]:((end[0]-start[0]) * n) + end[1]+1]


# def solution(n, left, right):
#     """
#     괜히 어렵게 풀었네 2차원 배열 예시를 보면 아래와 같이 나머지 + 1 와 몫 +1 값 중 가장 큰 수를 출력하면 됨
#     """
#     answer = []
#     for i in range(left,right+1):
#         answer.append(max(i//n,i%n)+1)
#     return answer


assert solution(3, 2, 5) == [3,2,2,3]
assert solution(4, 7, 14) == [4,3,3,3,4,4,4,4]
assert solution(4, 0, 2) == [1, 2, 3]
