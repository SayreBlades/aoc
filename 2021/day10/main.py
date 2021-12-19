import os

import numpy as np

HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')

pairs = {
    '[': ']',
    '(': ')',
    '<': '>',
    '{': '}',
}


def get_data(fname):
    with open(fname) as f:
        return [l.strip() for l in f]


def part1(fname):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    score = 0
    for idx, line in enumerate(get_data(fname)):
        arr = []
        for c2 in line:
            if not arr:
                arr.append(c2)
                continue
            c1 = arr[-1]
            if c2 in pairs.keys():
                arr.append(c2)
            elif pairs[c1] == c2:
                arr.pop()
            else:
                score += scores[c2]
                break
    return score


def part2(fname):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    tot_scores = []
    for line in get_data(fname):
        arr = []
        corrupt = False
        for c2 in line:
            if not arr:
                arr.append(c2)
                continue
            c1 = arr[-1]
            if c2 in pairs.keys():
                arr.append(c2)
            elif pairs[c1] == c2:
                arr.pop()
            else:
                corrupt = True
                break
        if not corrupt:
            score = 0
            auto_complete_chars = [pairs[o] for o in arr[::-1]]
            for c in auto_complete_chars:
               score *= 5
               score += scores[c]
            tot_scores.append(score)
    return int(np.median(tot_scores))


if __name__ == '__main__':
    print(part1(TEST_FILE))  # 26397
    print(part1(DATA_FILE))  # 243939
    print(part2(TEST_FILE))  # 288957
    print(part2(DATA_FILE))  # 2421222841
