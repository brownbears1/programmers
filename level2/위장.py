"""
최소 1개의 의상은 입어야 한다.
의상을 입을 때, 동일한 의상에서는 무조건 1개만 선택이 가능하다.

예제의
{
    'headgear': ['yellow_hat', 'green_turban'],
    'eyewear': ['blue_sunglasses']
}

에서 길이로 보면 headhear는 2, eyewear는 1이지만 선택을 안할 수 있어서 공집합 개념인 1을 더해 headhear의 길이는 3, eyewear의 길이는 2가 된다.
모든 조합의 수는 3 * 2 = 6 인데 여기에는 모든 선택을 하지 않은 공집합도 포함되어 있으므로 1을 빼주면 최소 1개를 선택하는 모든 조합의 수가 나오게 된다.

모든 조합의 수
0개 선택 시:
 1. 하나도 선택하지 않음
1개 선택 시:
 2. 'yellow_hat'
 3. 'green_turban'
 4. 'blue_sunglasses'
2개 선택 시:
 5. 'yellow_hat', 'blue_sunglasses'
 6. 'green_turban', 'blue_sunglasses'

총 합 6개에서 지문의 조건 중 최소 1개는 선택되어야 한다가 존재하므로 0개 선택 경우의 수인 1을 빼줌
"""

# from collections import Counter
#
#
# def solution(clothes):
#     answer = 1
#     for a in Counter(cloth[1] for cloth in clothes).values():
#         answer *= (a + 1)
#     return answer - 1


from collections import Counter
from functools import reduce


def solution(clothes):
    """
    reduce 사용
    """
    # 3번째 인자에 값을 주게 되면 1 * (y + 1)이 첫 연산이 됨
    return reduce(lambda x, y: x * (y + 1), Counter(cloth[1] for cloth in clothes).values(), 1) - 1


assert solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]) == 5
assert solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]) == 3
assert solution([['crow_mask', 'face1'], ['blue_sunglasses', 'face2'], ['smoky_makeup', 'face3']]) == 7
