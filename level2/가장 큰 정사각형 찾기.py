# def solution(board):
#     """
#     배열의 sum으로 진행하면 효율성 1,2,3 실패
#     사전에 0의 좌표를 찾고 검증하는 방식으로 하면 nested_sum보단 훨씬 빠르지 않을까 싶음
#     """
#     def nested_sum():
#         for i in range(y, y + size):
#             sum(board[i][x:x + size])
#         return sum(sum(board[i][x:x + size]) for i in range(y, y + size))
#
#     x_height = len(board[0])
#     y_height = len(board)
#     maximum_square = min(x_height, y_height)
#
#     for size in range(maximum_square, 0, -1):
#         target_square = size ** 2
#         x = 0
#         y = 0
#         while True:
#             if target_square == nested_sum():
#                 return target_square
#             if x + size < x_height:
#                 x += 1
#             elif y + size != y_height:
#                 x = 0
#                 y += 1
#             else:
#                 break
#
#     return 0


def solution(board):
    """
    시작 (x,y)에서 오른쪽 대각선으로 내려가고(x+1,y+1) 대각선 기준으로 왼쪽(x,y+1), 위(x+1,y), 좌측 대각선(x,y) 의 값이 전부 1이면 된다.
    즉, 3개의 값에서 최소값을 가져와 x+1,y+1에 +1을 더해주면 정사각형의 총 길이가 된다.
    만약 세개의 값 중, 1개라도 0이 있다면 이동한 정사각형은 0 + 1로 크기가 1인 정사각형이 된다.

    단 여기서 x+1, y+1 로 이동할 값이 0이라면 계산하지 않고 건너뛴다. 어차피 움직이지 못하는 곳을 계산할 필요가 없기 때문이다.
    """

    x_height = len(board[0])
    y_height = len(board)

    maximum_size = 0
    for y in range(1, y_height):
        for x in range(1, x_height):
            if not board[y][x]:
                continue
            board[y][x] = min(board[y-1][x-1], board[y][x-1], board[y-1][x]) + 1
            if maximum_size < board[y][x]:
                maximum_size = board[y][x]

    if not maximum_size and board[0][0]:
        return 1
    return maximum_size ** 2


assert solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) == 9
assert solution([[0,0,1,1],[1,1,1,1]]) == 4
assert solution([[0,0,0,0],[0,0,0,0]]) == 0
assert solution([[1,0],[0,0]]) == 1
