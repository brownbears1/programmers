"""
[가장 먼저 탈락하는 사람의 번호, 그 사람이 자신의 몇 번째 차례에 탈락하는지]

탈락하는 조건
1. 이전에 사용한 같은 단어 사용
2. 앞에서 사용한 문자와 다른 문자로 시작하는 단어 사용
"""


def solution(n, words):
    word_dict = {}
    last_chr = ''
    for i, word in enumerate(words):
        if word_dict.get(word, False) or (last_chr and last_chr != word[0]):
            return [i % n + 1,  i // n + 1]
        word_dict[word] = True
        last_chr = word[-1]

    return [0, 0]


# def solution(n, words):
#     """
#     짧게 표현할 순 있지만 주어지는 변수가 커지면 성능이 안나옴
#     """
#     for i in range(1, len(words)):
#         if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
#             return [i % n + 1,  i // n + 1]
#
#     return [0, 0]


assert solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3, 3]
assert solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0, 0]
assert solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3]
