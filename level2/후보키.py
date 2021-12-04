from itertools import combinations


# def solution(relation):
#     answer = 0
#     attr_size = len(relation[0])
#     keys = list(range(attr_size))
#
#     for i in range(1, attr_size + 1):
#         deletes = set()
#         for combination in list(combinations(keys, i)):
#             combination_attrs = []
#             for row in relation:
#                 combination_attrs.append(tuple(row[c] for c in combination))
#
#             if len(set(combination_attrs)) == len(combination_attrs):
#                 answer += 1
#                 deletes.update(combination)
#
#         for delete in deletes:
#             keys.remove(delete)
#
#     return answer


def solution(relation):
    attr_size = len(relation[0])
    keys = list(range(attr_size))
    candidate_keys = []

    for i in range(1, attr_size + 1):
        for combination in list(combinations(keys, i)):
            hist = []
            for row in relation:
                current_key = [row[c] for c in combination]
                if current_key in hist:
                    break
                else:
                    hist.append(current_key)
            else:
                for key in candidate_keys:
                    if set(key).issubset(set(combination)):
                        break
                else:
                    candidate_keys.append(combination)

    return len(candidate_keys)



# print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"],
#                 ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"],
#                 ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
# assert solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"],
#                  ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"],
#                  ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]) == 2

print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))

# assert solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]) == 3