"""
임의의 마을 간 다리는 무조건 존재 (= 주어진 모든 마을은 연결이 되어 있다)
마을 a, b 간에는 다리가 여러개 일 수도 있음 (= 그 중, 가중치가 가장 낮은 다리만 표시하면 문제풀기가 수월해짐)
시작은 무조건 1번 마을 (= 시작점은 고정)

prims 알고리즘을 사용하면 될 듯 하다. (XXXXXX)
- 여기서는 이동할 때마다 간선의 가중치를 더해야 하기 때문에 prims 알고리즘은 맞지 않음

다익스트라 알고리즘이네
- 하나의 점에서 시작해 모든 경로를 도달할 수 있는 최단 경로 찾기

그래프를 만들 때, 주의해야 할 점은 두 가지다.
1. 입력된 road의 데이터는 [마을1,마을2,가중치] 인데 마을1:마을2와 같은 식으로 담으면 안되고 마을1:마을2, 마을2:마을1 과 같이 담아야한다.
2. 마을 a, b 간의 다리가 여러개 일 수도 있어서 가중치가 가장 낮은 다리만 저장한다.

"""

import heapq
from collections import defaultdict


def solution(N, road, K):
    def dijkstra():
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        queue = []
        heapq.heappush(queue, [distances[start], start])

        while queue:
            current_distance, current_destination = heapq.heappop(queue)

            if distances[current_destination] < current_distance:
                continue

            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance
                if distance < distances[new_destination]:
                    distances[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])

        return distances

    graph = defaultdict(dict)
    start = 1
    for r in road:
        graph[r[0]][r[1]] = min(r[2], graph[r[0]].get(r[1], float('inf')))
        graph[r[1]][r[0]] = min(r[2], graph[r[1]].get(r[0], float('inf')))

    shortest_route = dijkstra()
    return len(list(filter(lambda k: shortest_route[k] <= K, shortest_route)))


assert solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3) == 4
assert solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4) == 4
