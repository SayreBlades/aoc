import os
from scipy.ndimage import find_objects

import numpy as np


HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    data = []
    with open(fname) as f:
        for l in f.readlines():
            data.append([int(c) for c in l if c.strip()])
    return np.array(data)


def part1(fname):
    data = get_data(fname)
    data = np.pad(data, 1, constant_values=9999)
    up = np.roll(data, 1, axis=0)
    down = np.roll(data, -1, axis=0)
    right = np.roll(data, 1, axis=1)
    left = np.roll(data, -1, axis=1)
    mask = ((data < up) & (data < down) & (data < left) & (data < right))
    return sum(data[mask]+1)


def part2(fname):
    data = get_data(fname)
    data = np.pad(data, 1, constant_values=9999)
    up = np.roll(data, 1, axis=0)
    down = np.roll(data, -1, axis=0)
    right = np.roll(data, 1, axis=1)
    left = np.roll(data, -1, axis=1)
    mask = ((data < up) & (data < down) & (data < left) & (data < right))
    data[data == 9] = -1
    new_mask = mask[1:-1, 1:-1]
    new_data = (data[1:-1, 1:-1] > -1) * 1
    components = []
    for y, x in np.stack(np.where(new_mask), axis=1):
        components.append(list(get_components(new_data, [(y, x)])))
    components = np.array([len(c) for c in components])
    components = components[components.argsort()[-3:]]
    return np.multiply.reduce(components)



def get_components(mat, locs):
    for y, x in locs:
        if x < 0 or x >= mat.shape[1]:
            continue
        if y < 0 or y >= mat.shape[0]:
            continue
        if mat[y, x] == 1:
            yield (y, x)
            mat[y, x] = 0
            locs = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
            for loc in get_components(mat, locs):
                yield loc


if __name__ == '__main__':
    print(part1(TEST_FILE))  # 15
    print(part1(DATA_FILE))  # 591
    print(part2(TEST_FILE))  # 1134
    print(part2(DATA_FILE))  # 1113424
