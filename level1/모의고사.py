def solution(answers):
    people_dict = {
        1: {'method': [1, 2, 3, 4, 5], 'count': 0},
        2: {'method': [2,1,2,3,2,4,2,5], 'count': 0},
        3: {'method': [3,3,1,1,2,2,4,4,5,5], 'count': 0}
    }

    for i, answer in enumerate(answers):
        for key in people_dict:
            if i == 0:
                people_dict[key]['len'] = len(people_dict[key]['method'])

            if people_dict[key]['method'][i % people_dict[key]['len']] == answer:
                people_dict[key]['count'] += 1

    max_count = max(people_dict.items(), key=lambda x: x[1]['count'])[1]['count']
    return [key for key in people_dict if people_dict[key]['count'] == max_count]


assert solution([1,2,3,4,5]) == [1]
assert solution([1,3,2,4,2]) == [1,2,3]
