"""
n명의 권투선수가 있으면,
1등은 n-1승 0패다.
2등은 n-2승 1패다.
3등은 n-3승 2패다.
꼴등은 0승 n-1패다.

플로이드-와샬 알고리즘을 사용하면 된다고 한다.

알고리즘을 사용하지 않고도 풀 수 있다.
1. 이긴 사람 위주, 진 사람 위주로 그래프 데이터를 2개 만든다.
2. 참가자는 1~n까지 존재하므로 n+1만큼 반복문을 진행한다.
3. 2번의 반복문을 진행하면서 참가자 i에게 이긴 명단을 이긴 사람 그래프에 그대로 업데이트한다.
4. 3번과 반대로 참가자 i에게 진 명단을 진 사람 그래프에 그대로 업데이트한다.
5. 3, 4번을 진행하면 이긴 명단, 진 명단이 전부 완성이 된다.
6. n+1만큼 반복문을 진행하면서 참가자 i가 이긴 명단 길이 + 진 명단 길이 가 주어진 사람 n - 1과 동일하면 개수를 올린다.
"""


from collections import defaultdict
from itertools import zip_longest


def solution(n, results):
    winner_graph, loser_graph = defaultdict(set), defaultdict(set)

    for result in results:
        loser_graph[result[1]].add(result[0])
        winner_graph[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winners, losers in zip_longest(loser_graph[i], winner_graph[i]):
            winner_graph[winners].update(winner_graph[i])
            loser_graph[losers].update(loser_graph[i])

    return sum(1 for i in range(1, n + 1) if len(winner_graph[i]) + len(loser_graph[i]) == n - 1)


def solution(n, results):
    """
    플로이드-와샬 알고리즘을 사용해 해결
    """
    # 승리 1, 패배 -1, 초기화 (또는 알 수 없음) 0
    board = [[0] * n for _ in range(n)]
    for winner, loser in results:
        winner -= 1
        loser -= 1
        board[winner][loser] = 1
        board[loser][winner] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1
                    elif board[i][k] == -1 and board[k][j] == -1:
                        board[i][j] = -1

    # 각 노드 점수판에 0(자기자신)만 있는 경우, 모든 선수와 경기를 했으므로 확실하게 순위를 정할 수 있음
    return sum(1 for i in range(n) if board[i].count(0) == 1)


assert solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]) == 2
