import os
from pprint import pprint

from collections import defaultdict

HERE = os.path.dirname(__file__)
TEST_FILE1 = os.path.join(HERE, 'input_test1.txt')
TEST_FILE2 = os.path.join(HERE, 'input_test2.txt')
TEST_FILE3 = os.path.join(HERE, 'input_test3.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    with open(fname) as f:
        return [line.strip().split('-') for line in f.readlines()]


def get_connected_nodes(edges, node):
    for n1, n2 in edges:
        if node == n1:
            yield n2
        if node == n2:
            yield n1


def traverse(edges, is_valid, path=None):
    if not path:
        path = ['start']
    node = path[-1]
    if node == 'end':
        return
    for no in get_connected_nodes(edges, node):
        new_path = path.copy()
        new_path.append(no)
        if not is_valid(new_path):
            continue
        if no == 'end':
            yield new_path
        for p in traverse(edges, is_valid, new_path):
            if not p:
                continue
            if p[-1] == 'end':
                yield p


def part1(fname):

    def is_valid(path):
        last = path[-1]
        return not (last.islower() and last in path[:-1])

    edges = get_data(fname)
    return len(list(traverse(edges, is_valid)))


def part2(fname):

    def is_valid(path):
        counts = defaultdict(lambda: 0)
        for p in path:
            if p.islower():
                counts[p] += 1
        start = counts['start']
        end = counts['end']
        rem = [v for k, v in counts.items() if k not in ('start', 'end')]
        return (
            start == 1 and
            end in (0, 1) and
            sum(rem) <= (len(rem) + 1)
        )

    edges = get_data(fname)
    return len(list(traverse(edges, is_valid)))


if __name__ == '__main__':
    print(part1(TEST_FILE1))  # 10
    print(part1(TEST_FILE2))  # 19
    print(part1(TEST_FILE3))  # 226
    print(part1(DATA_FILE))   # 4186

    print(part2(TEST_FILE1))  # 36
    print(part2(TEST_FILE2))  # 103
    print(part2(TEST_FILE3))  # 3509
    print(part2(DATA_FILE))   # 92111
