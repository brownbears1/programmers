class DisjointSet:
    def __init__(self, n):
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, root1, root2):
        self.parent[root2] = root1


def solution(n, costs):
    answer = 0
    disjoint_set = DisjointSet(n)

    for edge in sorted(costs, key=lambda cost: cost[2]):
        v, u, weight = edge
        root1 = disjoint_set.find(v)
        root2 = disjoint_set.find(u)
        if root1 != root2:
            disjoint_set.union(root1, root2)
            answer += edge[2]

    return answer