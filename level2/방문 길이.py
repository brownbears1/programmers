"""
좌표평면이 넘어가면 무시

흔히 길찾기처럼 하면 안됨
갔던 길과 왔던 길을 다시 찾아야 됨

아래 로직에서 해결한 순서는 다음과 같음
0. 이동할 좌표가 -5, 5 가 넘는지 비교
1. 시작 좌표와 도착 좌표를 정렬해서 변수에 저장
- 순서는 상관이 없으므로 정렬을 했다.
2. 왔던 길을 담고 있는 리스트에 1번에 저장한 변수의 좌표가 있는지 비교
3. 없다면 왔던 길 리스트에 저장
4. 좌표 이동
5. 왔던 길 리스트의 길이를 반환
"""


def solution(dirs):
    def moving(x, y):
        conv_x = standard[0] + x
        conv_y = standard[1] + y
        if conv_x < -5 or conv_x > 5 or conv_y < -5 or conv_y > 5:
            return

        coordinates = sorted([(standard[0], standard[1]), (conv_x, conv_y)])
        if coordinates not in answer:
            answer.append(coordinates)

        standard[0] += x
        standard[1] += y

    standard = [0, 0]
    answer = []
    movement = {
        'U': (0, -1),
        'D': (0, 1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    for d in dirs:
        moving(*movement[d])

    return len(answer)


assert solution("ULURRDLLU") == 7
assert solution("LULLLLLLU") == 7
assert solution('UDU') == 1
assert solution('LURD') == 4
assert solution('UUUUUUUUUUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR') == 20
