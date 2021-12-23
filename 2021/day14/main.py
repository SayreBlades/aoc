import os
from collections import Counter

HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    with open(fname) as f:
        poly, rules = f.read().split('\n\n')
        rules = dict([r.split(' -> ') for r in rules.split('\n') if r])
        return poly, rules


def genit(poly, rules):
    for i in range(len(poly)):
        cur_char = poly[i]
        yield cur_char
        if i+1 >= len(poly):
            return
        next_char = poly[i+1]
        found_char = rules.get(f'{cur_char}{next_char}')
        if found_char:
            yield found_char


def part1(fname, iters=1):
    poly, rules = get_data(fname)
    for _ in range(iters):
        poly = list(genit(poly, rules))
    char_freq = Counter(poly)
    min_char = max_char = None
    for k, v in char_freq.items():
        if not min_char or v < min_char[1]:
            min_char = (k, v)
        if not max_char or v > max_char[1]:
            max_char = (k, v)
    return max_char[1] - min_char[1]


if __name__ == '__main__':
    # print(get_data(TEST_FILE))
    print(part1(TEST_FILE, iters=10))  # 1588
    print(part1(DATA_FILE, iters=10))  # 2223
