"""
예제 2의 경우 ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.
로 BFS보단 DFS가 더 맞는거 같음
- BFS도 가능할듯?

주어진 항공권은 모두 사용해야 한다.

기존 dfs/bfs처럼 이동할 수 있는 리스트를 전부 붙이는게 아니라 알파벳 순으로 가장 빠른 공한 1개만 인접 노드 리스트에 넣는 형식으로 진행하자.

dfs로 결과의 역순으로 이동할 수 있는 공항을 전부 찾아나가고 초기에 설정한 graph에 키가 없거나 해당 공항을 도착해도 이동할 공항이 없으면 방문 공항에 넣는다.
최종 결과는 결과의 역순으로 쌓였으므로 이를 다시 역으로 돌리면 결과가 나온다.
"""

from collections import defaultdict


def solution(tickets):
    def dfs(graph, start):
        visited = []
        adjacency_nodes = [start]

        while adjacency_nodes:
            node = adjacency_nodes[-1]
            if not graph.get(node, None):
                visited.append(adjacency_nodes.pop())
            else:
                adjacency_nodes.append(graph[node].pop())

        visited.reverse()
        return visited

    graph = defaultdict(list)

    for departure, arrival in tickets:
        graph[departure].append(arrival)

    for key in graph:
        graph[key].sort(reverse=True)

    return dfs(graph, 'ICN')


assert solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"]
assert solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
assert solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]) == ["ICN", "B", "ICN", "A", "D", "A"]
assert solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]) == ["ICN", "B", "ICN", "A"]