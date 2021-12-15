import os

import tqdm
import dask
from dask.distributed import Client
from dask.distributed import progress
from dask.distributed import LocalCluster


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

    def process(i):
        sum = 0
        for d in data:
            for f in range(1, abs(d - i)+1):
                sum += f
        return sum

    cluster = LocalCluster(n_workers=8)
    client = Client(cluster)
    print(f"\ncheck job status at {client.dashboard_link}\n")
    futs = client.map(process, range(min(data), max(data)))
    progress(futs)
    return min(client.gather(futs))


if __name__ == "__main__":
    print(part1(TEST_FILE))  # 37
    print(part1(DATA_FILE))  # 364898
    print(part2(TEST_FILE))  # 168
    print(part2(DATA_FILE))  # 104149091
    input()
