"""
A
AA
AAA
AAAA
AAAAA
AAAAE
AAAAI
AAAAO
AAAAU
AAAE
AAAEA
AAAEE
AAAEI
AAAEO
AAAEU
AAAI
AAAIA
AAAIE
AAAII
AAAIO
AAAIU
AAAO
AAAOA
AAAOE
AAAOI
AAAOO
AAAOU
AAAU
AAAUA
AAAUE
AAAUI
AAAUO
AAAUU
AAE
AAEA
AAEAA
AAEAE
AAEAI
AAEAO
AAEAU
AAEE
AAEEA
AAEEE
AAEEI
AAEEO
AAEEU
AAEI
AAEIA
AAEIE
AAEII
AAEIO
AAEIU
AAEO
.
.
.
UUUIU
UUUO
UUUOA
UUUOE
UUUOI
UUUOO
UUUOU
UUUU
UUUUA
UUUUE
UUUUI
UUUUO
UUUUU

에서 계속 숫자 매기면서 아래와 같은 순서가 반복되는 것을 볼 수 있다.

xxxxA -> xxxxE -> xxxxI -> xxxxO -> xxxxU 는 1씩 증가
- AAAAA (5) -> AAAAE (6) -> AAAAI (7) -> AAAAO (8) -> AAAAU (9)

xxxA -> xxxE -> xxxI -> xxxO -> xxxU 는 6씩 증가
- AAAA (4) -> AAAE (10) -> AAAI (16) -> AAAO (22) -> AAAU (28)

xxA -> xxE -> xxI -> xxO -> xxU 는 31씩 증가
- AAA (3) -> AAE (34) -> AAI (65) -> AAO (96) -> AAU (127)

1, 6, 31, x, xx, xxx, ... 와 같이 증가하는데 여기서 규칙이 5의 배수로 늘어나는 것을 볼 수 있으므로 아래와 같이 다시 표현할 수 있다.
1) 1,  6,  31,  156, ...
2)  5,  25,  125,  ...
3)    x5,  x5


2번째는 첫째항이 5이고 등비는 5이므로 5^n으로 표현할 수 있고, 1번째는 2번째 등비수열의 합이므로 아래와 같이 표현이 가능하다.

1 + { 5 * (5^(n-1) -1) / (5 - 1) }
= 1 + (5^n-5)/4

이제 해당 식에 위 숫자들을 대입해보면 동일하게 나오는 것을 볼 수 있다.
n = 1 일 때,
1 + (5-5)/4 = 1
n = 2 일 때,
1 + (25-5)/4 = 6
n = 3 일 때,
1 + (125-5)/4 = 31


반복 패턴을 찾았으니 식을 대입하고 마지막에 1을 더해준다. 1을 더하는 이유는 해당 자리에 공백이 오는 경우의 수이다.



어렵게 풀고 다른 사람 풀이 보니까 황당하네
"""


def solution(word):
    _dict = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4,
    }

    _pattern = [int(1 + (5 ** i - 5) / 4) for i in range(5, 0, -1)]
    return sum(_dict[w] * _pattern[i] + 1 for i, w in enumerate(word))


assert solution("AAAAE") == 6
assert solution("AAAE") == 10
assert solution("I") == 1563
assert solution("EIO") == 1189
