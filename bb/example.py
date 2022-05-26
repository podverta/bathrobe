candidates = [
    {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62,
                               "computer_science": 48}, "extra_scores":0},
    {"name": "Fedya",  "scores": {"math": 33, "russian_language": 95,
                               "computer_science": 42},  "extra_scores":2},
    {"name": "Petya",  "scores": {"math": 25, "russian_language": 33,
                               "computer_science": 34},  "extra_scores":1},
    {"name": "Yulia", "scores": {"math": 33, "russian_language": 62,
                                 "computer_science": 48}, "extra_scores": 0},
    {"name": "Ura", "scores": {"math": 87, "russian_language": 95,
                                 "computer_science": 42}, "extra_scores": 2},
    {"name": "Stepan", "scores": {"math": 11, "russian_language": 33,
                                 "computer_science": 34}, "extra_scores": 1}
]



new_candidates = {}
sorted_candidates = []
def sum_score(candidates):
    for candidate in candidates:
        name = candidate['name']
        scores = sum([candidate['scores']['math'] + candidate['scores']['russian_language'] +
                 candidate['scores']['computer_science'] + candidate['extra_scores']])
        new_candidates[name] = scores
    for i in sorted(new_candidates.items(), key=lambda v: v[1], reverse=True):
        sorted_candidates.append(i)



if __name__ == '__main__' :
    sum_score(candidates)
    print(new_candidates)
    print(sorted_candidates)


