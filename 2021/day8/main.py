import os
from collections import defaultdict


HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    data = None
    with open(fname) as f:
        data = f.readlines()
    for d in data:
        input, output = d.split('|')
        v = ([o.strip() for o in input.split(' ') if o],
             [o.strip() for o in output.split(' ') if o])
        yield v


def part1(fname):
    data = list(get_data(fname))
    outputs = [o for _, o1 in data for o in o1]
    count = 0
    for o in outputs:
        if len(o) in (2, 3, 4, 7):
            count += 1
    return count


def create_num_map(words):
    len_map = defaultdict(list)
    for v in words:
        len_map[len(v)].append(set(v))
    num_map = {}
    num_map[1] = len_map[2][0]
    num_map[7] = len_map[3][0]
    num_map[4] = len_map[4][0]
    num_map[8] = len_map[7][0]
    for num in len_map[5]:
        if len(num - num_map[1]) == 3:
            num_map[3] = num
        elif len(num - num_map[4]) == 2:
            num_map[5] = num
        else:
            num_map[2] = num
    for num in len_map[6]:
        if len(num - num_map[3]) == 1:
            num_map[9] = num
        elif len(num - num_map[5]) == 1:
            num_map[6] = num
        else:
            num_map[0] = num
    return num_map


def lookup(val, num_map):
    val = set(val)
    for k, v in num_map.items():
        if len(val - v) or len(v - val):
            continue
        return k
    raise Exception((num_map, val))


def part2(fname):
    data = list(get_data(fname))
    sum = 0
    for inputs, outputs in data:
        num_map = create_num_map(inputs + outputs)
        num = int("".join([str(lookup(o, num_map)) for o in outputs]))
        sum += num
    return sum


if __name__ == '__main__':
    print(part1(TEST_FILE))  # 26
    print(part1(DATA_FILE))  # 383
    print(part2(TEST_FILE))  # 61229
    print(part2(DATA_FILE))  # 998900
