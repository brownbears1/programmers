"""
이건 잘 모르겠음.. bfs로 풀면 된다고 하는데 효율성 통과하네?
"""
from collections import deque


def solution(maps):
    return bfs(maps)


def bfs(maps):
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    dist = [[-1] * len(maps[0]) for _ in range(len(maps))]

    dist[0][0] = 1
    q = deque([(0, 0)])
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if dist[ny][nx] == -1 and maps[ny][nx] == 1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    q.append((ny, nx))
    return dist[-1][-1]


assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11
assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1
