"""
문제에서 중복되는 원소가 없는 튜플이라 했음
표현식을 보면 길이의 순서대로 쌓이는 것을 보이고 가장 길이가 긴 원소의 집합에서 순서만 조정하면 답이 됨

1. 원소의 길이 순서대로 정렬
2. 길이가 2 이상일 때부터 현재 {원소의 집합 - 이전 원소의 집합} 을 하고 나오는 나머지 값을 추가함
- 길이가 n=1, subset_list[n] = answer[n-1]
- 길이가 n>=2,{subset_list[n] - subset_list[n-1]} = answer[n-1]
"""


def solution(s):
    answer = []
    subset_list = sorted(s.lstrip('{').rstrip('}').split('},{'), key=len)

    for i in range(len(subset_list)):
        subset = set(subset_list[i].split(','))
        if i == 0:
            answer.append(int(subset.pop()))
            continue
        pre_subset = set(subset_list[i - 1].split(','))
        answer.append(int((subset - pre_subset).pop()))

    return answer


assert solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4]
assert solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4]
assert solution("{{20,111},{111}}") == [111, 20]
assert solution("{{123}}") == [123]
assert solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1]
