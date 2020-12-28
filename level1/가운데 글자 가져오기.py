def solution(s):
    s_len = len(s)
    return s[(s_len-1)//2:s_len//2+1]


# def solution(s):
#     s_length = len(s)
#
#     if s_length % 2 == 0:
#         index = int(s_length / 2)
#         answer = s[index - 1:index + 1]
#     else:
#         answer = s[int(s_length / 2)]
#
#     return answer

assert solution('abcde') == 'c'
assert solution('qwer') == 'we'
