import os

import numpy as np

HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    with open(fname) as f:
        data = []
        for line in f:
            data.append([int(c) for c in line if c.strip()])
        return np.array(data)


def add_neighbors(mask):
    add_mask = np.pad(mask, 1)
    res = np.zeros(add_mask.shape)
    right = np.roll(add_mask, 1, axis=1)
    left = np.roll(add_mask, -1, axis=1)
    up = np.roll(add_mask, 1, axis=0)
    up_left = np.roll(up, -1, axis=1)
    up_right = np.roll(up, 1, axis=1)
    down = np.roll(add_mask, -1, axis=0)
    down_left = np.roll(down, -1, axis=1)
    down_right = np.roll(down, 1, axis=1)
    res += (up_left   + up   + up_right  )
    res += (left      +        right     )
    res += (down_left + down + down_right)
    return res[1:-1, 1:-1].astype('int')


def part1(fname, passes = 100):
    data = get_data(fname)
    flashes = 0
    for _ in range(passes):
        data += 1
        mask = (data > 9) * 1
        mask_final = mask.copy()
        data = data * ((mask_final + 1) % 2)
        while sum(sum(mask)) > 0:
            neighbors = add_neighbors(mask)
            data += neighbors
            new_mask = (data > 9) * 1
            mask =  ((new_mask - mask_final) > 0) * 1
            mask_final = mask_final | mask
            data = data * ((mask_final + 1) % 2)
        flashes += sum(sum(data == 0))
    return flashes


def part2(fname):
    data = get_data(fname)
    iter = 0
    while True:
        iter += 1
        data += 1
        mask = (data > 9) * 1
        mask_final = mask.copy()
        data = data * ((mask_final + 1) % 2)
        while sum(sum(mask)) > 0:
            neighbors = add_neighbors(mask)
            data += neighbors
            new_mask = (data > 9) * 1
            mask =  ((new_mask - mask_final) > 0) * 1
            mask_final = mask_final | mask
            data = data * ((mask_final + 1) % 2)
        if np.all(data == 0):
            return iter


if __name__ == '__main__':
    print(part1(TEST_FILE, 100))  # 1656
    print(part1(DATA_FILE, 100))  # 1585
    print(part2(TEST_FILE))       # 195
    print(part2(DATA_FILE))       # 382
