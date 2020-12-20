def solution(board, moves):
    bucket = []
    answer = 0

    for move in moves:
        move -= 1
        for b in board:
            doll = b[move]
            if doll:
                bucket.append(doll)
                b[move] = 0
                break

        if len(bucket) > 1:
            if bucket[-1] == bucket[-2]:
                answer += 2
                del bucket[-2:]

    return answer


assert solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) == 4
