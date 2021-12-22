import os
import collections

import numpy as np
from PIL import Image

HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')

Coords = collections.namedtuple('Coords', ['x', 'y'])

def get_data(fname):
    dots = []
    folds = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif 'fold' in line:
                axis, val = line.replace('fold along ', '').split('=')
                folds.append((axis, int(val)))
            else:
                x, y = [int(o) for o in line.split(',')]
                dots.append(Coords(x, y))
    return dots, folds


def part1(fname):
    dots, folds = get_data(fname)
    max_x = max_y = 0
    for x, y in dots:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    data = np.zeros((max_y+1, max_x+1))
    for x, y in dots:
        data[y][x] = 1

    fold_ax, fold_val = folds[0]
    res = None
    if fold_ax == 'y':
        top = data[:fold_val, :]
        bottom = data[fold_val+1:, :]
        res = ((top + bottom[::-1, :]) > 0) * 1
    else:
        left = data[:, :fold_val]
        right = data[:, fold_val+1:]
        res = ((left + right[:, ::-1]) > 0) * 1
    return sum(sum(res))


def part2(fname):
    dots, folds = get_data(fname)
    max_x = max_y = 0
    for x, y in dots:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    data = np.zeros((max_y+1, max_x+1))
    for x, y in dots:
        data[y][x] = 1

    for fold_ax, fold_val in folds:
        if fold_ax == 'y':
            rem = (data.shape[0] + 1) % 2
            data = np.pad(data, ((0, rem), (0, 0)), mode='constant')
            top = data[:fold_val, :]
            bottom = data[fold_val+1:, :]
            data = ((top + bottom[::-1, :]) > 0) * 1
        else:
            rem = (data.shape[1] + 1) % 2
            data = np.pad(data, ((0, 0), (0, rem)), mode='constant')
            left = data[:, :fold_val]
            right = data[:, fold_val+1:]
            data = ((left + right[:, ::-1]) > 0) * 1
    return data


if __name__ == '__main__':
    # pprint(get_data(TEST_FILE))
    print(part1(TEST_FILE))  # 17
    print(part1(DATA_FILE))  # 759
    print(part2(TEST_FILE))
# [[1 1 1 1 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 1 1 1 1]
#  [0 0 0 0 0]
#  [0 0 0 0 0]]
    print(part2(DATA_FILE))
# [[1     1   1 1 1 1     1 1     1 1 1     1 1 1 1   1     1   1 1 1     1 1 1    ]
#  [1     1   1         1     1   1     1         1   1   1     1     1   1     1  ]
#  [1 1 1 1   1 1 1     1         1     1       1     1 1       1     1   1     1  ]
#  [1     1   1         1         1 1 1       1       1   1     1 1 1     1 1 1    ]
#  [1     1   1         1     1   1   1     1         1   1     1         1   1    ]
#  [1     1   1 1 1 1     1 1     1     1   1 1 1 1   1     1   1         1     1  ]]
