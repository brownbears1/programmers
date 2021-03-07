"""
이상한 공식을 찾으려고 하니까 문제가 안풀림.
2차원 배열을 만든 다음 수직, 수평, 대각선 으로 계속 움직이면 됨.
삼각형에 값을 다 채우면 최대값은 주어진 n에 대해 1+2+3+...+(n-1)+n 이다.
즉, sum(range(n+1)) 이 나올때까지 해당 로직을 실행하면 됨

삼각형의 시작 배열 인덱스는 (0,0), (1, 2), (2, 4) ... 이다.

1. 수직으로 배열의 끝 또는 값이 있을때까지 계속 내려가면서 채움
2. 수평으로 배열의 끝 또는 값이 있을때까지 계속 오른쪽으로 가면서 채움
3. 대각선으로 값이 있을때까지 계속 왼쪽 대각선으로 올라가면서 채움
4. 채워야 하는 숫자가 주어진 값의 합보다 작다면 1~3번 반복
"""


def solution(n):
    def down(row, col, number):
        while not(row == n or snails[row][col]):
            snails[row][col] = number
            row += 1
            number += 1

        return number, row - 1, col

    def side(row, col, number):
        while not(col == n or snails[row][col]):
            snails[row][col] = number
            col += 1
            number += 1
        return number, row, col - 1

    def diagonal(row, col, number):
        while not snails[row][col]:
            snails[row][col] = number
            row -= 1
            col -= 1
            number += 1
        return number, row, col

    snails = [list(map(int, '0' * (i + 1))) for i in range(n)]
    number = 1
    row = 0
    col = 0
    max_num = sum(range(n+1))

    while number < max_num + 1:
        number, row, col = down(row, col, number)
        number, row, col = side(row, col + 1, number)
        number, row, col = diagonal(row - 1, col - 1, number)

        row += 2
        col += 1

    result = []
    for snail in snails:
        result.extend(snail)

    return result


assert solution(4) == [1,2,9,3,10,8,4,5,6,7]
assert solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
assert solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
