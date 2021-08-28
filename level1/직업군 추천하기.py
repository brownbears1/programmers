"""
노가다성 문제 너무 귀찮아
"""


def solution(table, languages, preference):
    table_dict = {}
    _max = -1
    answer = ''
    language_dict = {language: p for language, p in zip(languages, preference)}

    for t in table:
        a = t.split(' ')
        table_dict[a[0]] = a[1:]

    for key, value in table_dict.items():
        _sum = 0
        for language_key, p in language_dict.items():
            try:
                _sum += (5 - value.index(language_key)) * p
            except:
                pass
        if _max < _sum:
            _max = _sum
            answer = key
        elif _max == _sum:
            answer = min(answer, key)

    return answer


assert solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]) == "HARDWARE"
assert solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]) == "PORTAL"
