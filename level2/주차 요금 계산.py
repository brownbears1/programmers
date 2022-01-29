import math
from collections import defaultdict


def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees

    temp_car_dict = {}
    car_parking_time = defaultdict(int)
    car_parking_fee = {}

    for record in records:
        time_, car_number, history = record.split(' ')
        hours, minutes = map(int, time_.split(':'))
        total_minutes = (hours * 60) + minutes

        if history == 'IN':
            temp_car_dict[car_number] = total_minutes
        else:
            in_times = temp_car_dict.pop(car_number)
            car_parking_time[car_number] += total_minutes - in_times

    # 출차를 하지 않은 차 내역 조사
    for car_number, in_times in temp_car_dict.items():
        total_minutes = (23 * 60) + 59
        car_parking_time[car_number] += total_minutes - in_times

    # 요금 계산
    for car_number, total_time in car_parking_time.items():
        extra_parking_time = total_time - default_time
        car_parking_fee[car_number] = default_fee

        if extra_parking_time <= 0:
            continue

        car_parking_fee[car_number] += int(math.ceil(extra_parking_time / unit_time)) * unit_fee

    return list(map(lambda x: x[1], sorted(car_parking_fee.items(), key=lambda x: x[0])))


assert solution([180, 5000, 10, 600],
                ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                 "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN",
                 "23:00 5961 OUT"]) == [14600, 34400, 5000]
assert solution([120, 0, 60, 591],
                ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT",
                 "23:58 3961 IN"]) == [0, 591]
assert solution([1, 461, 1, 10], ["00:00 1234 IN"]) == [14841]
