"""
쿼드트리 - 2^n x 2^n 크기로 커짐

예제 [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
를 보면
가로 길이가 4, 2, 1 로 줄어들면서 값을 계산한다.
즉 길이가 /2 로 줄어들면서 더이상 나눠지지 않을 때까지 계산하는 로직을 짠다.

가로 길이가 2이면 총 4개의 정사각형에 대해 값을 비교해야 한다. 4개의 정사각형에 대한 x,y 좌표는 아래와 같다.
(0,0), (0,2), (2,0), (2,2)

이를 미지수 x, y로 계산식을 만들면 아래와 같다.
길이: s
x축: x
y축: y

(x,y)
(x,y+s)
(x+s,y)
(x+s,y+s)

위 공식을 대입하여 재귀를 실행하면 쉽게 만들 수 있다.

요약:
1. (x,y), (x,y+s), (x+s,y), (x+s,y+s) 와 같이 나눠짐
2. s가 더이상 나눠지지 않을 때까지, 가로의 길이를 2로 나눔
3. 해당 블록이 전부 1이거나 전부 0이면 더이상 나누지 않음
"""


def solution(arr):
    def nested_sum(i, j, _range):
        return sum(
            col for _, row in enumerate(arr[i:_range+i])
            for _, col in enumerate(row[j:_range+j])
        )

    def quad(i, j, _range):
        if not _range:
            return
        area_sum = nested_sum(i, j, _range)

        if area_sum == _range ** 2:
            answer[1] += 1
            return
        elif not area_sum:
            answer[0] += 1
            return

        next_range = _range // 2

        quad(i, j, next_range)
        quad(i, j + next_range, next_range)
        quad(i + next_range, j, next_range)
        quad(i + next_range, j + next_range, next_range)

    answer = [0, 0]
    quad(0, 0, len(arr))
    
    return answer


assert solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) == [4, 9]
assert solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]) == [10, 15]
