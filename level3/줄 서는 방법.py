"""
모든 순열의 조합을 구하면 시간초과발생

n번째의 갯수는 (n-1)! * n이다. 즉, n!/n = (n-1)! 을 하면 자릿수의 범위를 찾을 수 있다.
다음 주어진 k번째를 찾으려면 (k-1) // (n-1)! 를 하면 [1, 2, 3, ..., n]번째에 위치한 인덱스를 찾을 수 있다.
k-1을 한 이유는 1부터 시작하는 자연수이기 때문이다.

다음 범위를 찾기 위해선 (k-1)를 (n-1)!로 나눈 나머지를 가져가면 된다.


풀이순서
1. 주어진 n에 맞게 1,2,3,...,n까지 리스트 생성
2. 자연수인 k를 1 빼기
3. (n-1)!계산
4. 인덱스를 구하기 위해 k // (n-1)! 계산
5. 1번의 리스트에서 4번 인덱스 제거 후 값 answer에 추가
6. k를 (n-1)! 로 나눈 나머지 값으로 대체
7. (n-1 - 1)! 계산 후 4~6번 까지 반복
"""

from itertools import permutations
#
#
# def solution(n, k):
#     """
#     시간초과 발생
#     """
#     return list(permutations(range(1, n+1), n))[k-1]


from math import factorial


def solution(n, k):
    i = 0
    # 1부터 시작하기 때문에 1 빼줌
    k -= 1
    answer = []
    lst = list(range(1, n + 1))

    while lst:
        f = factorial(n - 1 - i)
        index = k // f
        answer.append(lst.pop(index))
        k %= f
        i += 1

    return answer


print(solution(4, 7))
assert solution(3, 5) == [3, 1, 2]
