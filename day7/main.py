import os
import tqdm

HERE = os.path.dirname(__file__)
TEST_FILE = os.path.join(HERE, 'input_test.txt')
DATA_FILE = os.path.join(HERE, 'input.txt')


def get_data(fname):
    with open(fname, 'r') as f:
        data = "".join(f.readlines())
        return [int(d) for d in data.split(',')]


def part1(fname):
    data = get_data(fname)
    results = {}
    for i in range(min(data), max(data)):
        sum = 0
        for d in data:
            sum += abs(d - i)
        results[i] = sum
    return min(results.values())


def part2(fname):
    data = get_data(fname)
    results = {}
    for i in tqdm.tqdm(range(min(data), max(data))):
        sum = 0
        for d in data:
            for f in range(1, abs(d - i)+1):
                sum += f
        results[i] = sum
    return min(results.values())


if __name__ == "__main__":
    print(part1(TEST_FILE))  # 37
    print(part1(DATA_FILE))  # 364898
    print(part2(TEST_FILE))  # 168
    print(part2(DATA_FILE))  # 104149091
