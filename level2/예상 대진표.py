"""
최대가 2^20 인걸 보면 리스트에 값을 다 담지말고 수학적으로 풀어야 되는듯

1 = 1 // 2 + 1 % 2 = 1
2 = 2 // 2 + 2 % 2 = 1
3 = 3 // 2 + 3 % 2 = 2
4 = 4 // 2 + 4 % 2 = 2
5 = 5 // 2 + 5 % 2 = 3
6 = 6 // 2 + 6 % 2 = 3
7 = 7 // 2 + 7 % 2 = 4
8 = 8 // 2 + 8 % 2 = 4

와 같이 바로 인접한 수가 같은 것을 볼 수 있으므로 이를 같을 때까지 반복하면 됨
예제의 수 3, 7을 위 식에 대입하면 아래와 같다

round 1)
3 // 2 + 3 % 2 = 1 + 1 = 2
7 // 2 + 7 % 2 = 3 _ 1 = 4

round 2)
2 // 2 + 2 % 2 = 1 + 0 = 1
4 // 2 + 4 % 2 = 2 + 0 = 2

round 3)
1 // 2 + 1 % 2 = 0 + 1 = 1
2 // 2 + 2 % 2 = 1 + 0 = 1

3번째에 3, 7은 만나게 된다.

"""


def solution(n, a, b):
    cnt = 0
    while a != b:
        a = sum(divmod(a, 2))
        b = sum(divmod(b, 2))
        cnt += 1
    return cnt


assert solution(8, 4, 7) == 3
