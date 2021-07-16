def solution(s):
    if s.isdecimal():
        return int(s)
    _key = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for k, v in _key.items():
        s = s.replace(k, v)

    return int(s)


assert solution('one4seveneight') == 1478
assert solution('23four5six7') == 234567
assert solution('2three45sixseven') == 234567
assert solution('123') == 123
