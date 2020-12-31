def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        is_vaild = True
        index = 0
        for s in skill_tree:
            if s in skill:
                if s == skill[index]:
                    index += 1
                else:
                    is_vaild = False
                    break
        if is_vaild:
            result += 1

    return result


assert solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2
