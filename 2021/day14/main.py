import os
from collections import defaultdict

from numba import njit
from tqdm import tqdm


HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    with open(fname) as f:
        poly, rules = f.read().split('\n\n')
        rules = dict([r.split(' -> ') for r in rules.split('\n') if r])
        return poly, rules


def part1(fname, iters=1):
    poly, rules = get_data(fname)
    pairs = defaultdict(lambda: 0)
    for i, ch in enumerate(poly):
        if i + 1 < len(poly):
            pairs[ch+poly[i+1]] += 1
    for _ in range(iters):
        new_pairs = defaultdict(lambda: 0)
        for k, v in pairs.items():
            rule = rules.get(k)
            if not rule:
                new_pairs[k] = v
            else:
                new_pairs[k[0]+rule] += v
                new_pairs[rule+k[1]] += v
        pairs = new_pairs
    counts = defaultdict(lambda: 0)
    for k, v in pairs.items():
        counts[k[0]] += v
        counts[k[1]] += v
    counts[poly[0]] += 1
    counts[poly[-1]] += 1
    return (max(counts.values()) - min(counts.values())) // 2



if __name__ == '__main__':
    # print(get_data(TEST_FILE))
    print(part1(TEST_FILE, iters=10))  # 1588
    print(part1(DATA_FILE, iters=10))  # 2223
    print(part1(TEST_FILE, iters=40))  # 2188189693529
    print(part1(DATA_FILE, iters=40))  # 2566282754493
