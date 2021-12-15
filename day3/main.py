import numpy as np


def get_data(fname):
    data = None
    with open(fname) as f:
        data = [[int(n) for n in line.strip()] for line in f.readlines()]
    return np.array(data)


def part1(data):
    gamma = (data.mean(axis=0) > 0.5) * 1
    gamma = ''.join([str(o) for o in gamma])
    gamma = int(gamma, 2)
    # print(gamma)
    epsilon = (data.mean(axis=0) < 0.5) * 1
    epsilon = ''.join([str(o) for o in epsilon])
    epsilon = int(epsilon, 2)
    # print(epsilon)
    return gamma * epsilon


def part2_recurse(data, find='oxy', idx=0):
    if len(data) == 1 or idx == data.shape[1]:
        return data[0]
    val = None
    if find == 'oxy':
        val = (data[:, idx].mean() >= 0.5) * 1
    else:
        val = (data[:, idx].mean() < 0.5) * 1
    data = data[data[:, idx] == val]
    return part2_recurse(data, find, idx+1)


def part2(data):
    oxygen = part2_recurse(data, find='oxy')
    oxygen = ''.join([str(o) for o in oxygen])
    oxygen = int(oxygen, 2)
    # print(oxygen)
    co2 = part2_recurse(data, find='co2')
    co2 = ''.join([str(o) for o in co2])
    co2 = int(co2, 2)
    # print(co2)
    return oxygen * co2


print(part2(get_data('input')))
