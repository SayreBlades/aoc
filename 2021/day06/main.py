import os
import numpy as np

HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    data = None
    with open(fname) as f:
        data = f.readlines()
    return [int(i) for i in "".join(data).split(',')]


def iter_next(data):
    zeros = sixs = 0
    for k, v in data:
        if k == 7:
            sixs = sixs+v
        elif k == 0:
            zeros = v
            sixs = sixs+v
        else:
            yield k-1, v
    if sixs:
        yield 6, sixs
    if zeros:
        yield 8, zeros


def main(fname, num):
    data = get_data(fname)
    data = np.stack(np.unique(data, return_counts=True), axis=1)
    for _ in range(num):
        data = list(iter_next(data))
    return sum([v for _, v in data])


if __name__ == '__main__':
    print(main(TEST_FILE, num=80))     # 5934
    print(main(DATA_FILE, num=80))     # 379114
    print(main(TEST_FILE, num=256))    # 26984457539
    print(main(DATA_FILE, num=256))    # 1702631502303
