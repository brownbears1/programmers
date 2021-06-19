"""
words에 있는 단어로만 변환할 수 있으므로 words에 target이 없으면 0 바로 반환
words 중간에 target이 나온다면 그 뒤의 단어들은 볼 필요도 없다. (중복 단어 없음)

tc가 너무 적어서 테스트에서는 꺠지는데 채점하면 통과한다.
"""
#
# from collections import deque
#
#
# def solution(begin, target, words):
#     def bfs(graph, start):
#         visited_nodes = []
#         adjacency_nodes = deque([start])
#         answer = -1
#
#         while adjacency_nodes:
#             node = adjacency_nodes.popleft()
#             if node not in visited_nodes:
#                 answer += 1
#                 visited_nodes.append(node)
#
#                 for _node in graph[node]:
#                     if _node in visited_nodes and _node in graph[node]:
#                         continue
#                     cnt = 0
#                     for i in range(len(node)):
#                         if visited_nodes and visited_nodes[-1][i] != node[i]:
#                             cnt += 1
#                     if cnt and cnt != 1:
#                         continue
#
#                     adjacency_nodes.append(_node)
#
#                     if target == _node:
#                         return answer
#
#     if target not in words:
#         return 0
#
#     graph = {}
#     base_words = deque(words)
#     base_words.appendleft(begin)
#
#     for word in base_words:
#         edges = []
#         for target_word in base_words:
#             if word == target_word:
#                 continue
#             cnt = 0
#             for i in range(len(word)):
#                 if target_word[i] != word[i]:
#                     cnt += 1
#
#             if cnt == 1:
#                 edges.append(target_word)
#         graph[word] = edges
#
#         if word == target:
#             break
#
#     return bfs(graph, begin)


from collections import deque


def solution(begin, target, words):
    def can_change(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        return cnt == 1

    def bfs(begin, target, words):
        check = [False for _ in range(len(words))]
        answer = 0
        dq = deque([begin])

        while len(dq) > 0:
            answer += 1
            for k in range(len(dq)):
                curWord = dq.pop()

                for i, word in enumerate(words):
                    if not check[i] and can_change(curWord, word):
                        check[i] = True
                        dq.append(word)
                        if word == target:
                            return answer

        return 0
    return bfs(begin, target, words)


assert solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
assert solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]) == 0
