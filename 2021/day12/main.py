import os

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


def traverse(edges, path=None):
    if not path:
        path = ['start']
    node = path[-1]
    if node == 'end':
        return
    for no in get_connected_nodes(edges, node):
        if no.islower() and no in path:
            continue
        new_path = path.copy()
        new_path.append(no)
        if no == 'end':
            yield new_path
        for p in traverse(edges, new_path):
            if not p:
                continue
            if p[-1] == 'end':
                yield p


def part1(fname):
    edges = get_data(fname)
    return len(list(traverse(edges)))


if __name__ == '__main__':
    print(part1(TEST_FILE1))  # 10
    print(part1(TEST_FILE2))  # 19
    print(part1(TEST_FILE3))  # 19
    print(part1(DATA_FILE))   # 19
