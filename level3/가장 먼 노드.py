"""
간선은 양방향(cycle)이며 weight는 전부 1
가장 멀리 있는 모든 노드를 찾는 문제
모든 노드를 방문하고 1에서 부터 간선의 가중치를 더해 해당 노드까지의 거리를 구하면 된다.

다익스트라 알고리즘으로 모든 노드를 방문, 간선의 가중치를 찾은 다음, 가장 멀리 떨어져 있는 노드들의 개수를 출력한다.

다익스트라 말고도 다른 그래프 알고리즘으로도 해결할 수 있을 것 같다.
"""
import heapq
import sys
from collections import defaultdict


def solution(n, edge):
    def dijkstra(start):
        distances = {node: sys.maxsize for node in graph}
        distances[start] = 0
        queue = []
        heapq.heappush(queue, (distances[start], start))

        while queue:
            current_distance, node = heapq.heappop(queue)
            if distances[node] < current_distance:
                continue

            for adjacency_node, distance in graph[node].items():
                weighted_distance = current_distance + distance
                if weighted_distance < distances[adjacency_node]:
                    distances[adjacency_node] = weighted_distance
                    heapq.heappush(queue, (weighted_distance, adjacency_node))
        return distances

    graph = defaultdict(dict)

    for e in edge:
        graph[e[0]][e[1]] = 1
        graph[e[1]][e[0]] = 1

    dijkstra_result_dict = dijkstra(1)
    result = sorted(dijkstra_result_dict.values(), reverse=True)
    return result.count(result[0])


assert solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3
