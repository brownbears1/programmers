from collections import OrderedDict, Counter


def solution(id_list, report, k):
    counter = Counter(id_list)
    report_dict = OrderedDict({key: set() for key in id_list})

    for r in set(report):
        reporter, bad_user = r.split(' ')
        counter[bad_user] += 1
        report_dict[reporter].add(bad_user)

    blacklist = set(map(lambda x: x[0], filter(lambda x: x[1] > k, counter.items())))

    return [len(blacklist.intersection(value)) for value in report_dict.values()]


print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
assert solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2) == [2,1,1,0]
assert solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3) == [0,0]

