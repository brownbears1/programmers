def solution(s):
    def check(target):
        stack = []
        for bracket in target:
            if not stack:
                stack.append(bracket)
                continue
            if bracket == ')':
                if stack.pop() != '(':
                    return False
            elif bracket == '}':
                if stack.pop() != '{':
                    return False
            elif bracket == ']':
                if stack.pop() != '[':
                    return False
            else:
                stack.append(bracket)

        return not stack

    answer = 0
    length = len(s)
    for i in range(length):
        if check(s[i:length] + s[0:i]):
            answer += 1
    return answer


assert solution("[](){}") == 3
assert solution("}]()[{") == 2
assert solution("[)(]") == 0
assert solution("}}}") == 0
assert solution("([{)}]") == 0
