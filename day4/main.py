import numpy as np


def get_data(fname):
    data = None
    with open(fname) as f:
        data = f.read()
    data = data.split('\n\n')
    numbers = np.array([int(n) for n in data[0].split(',')]).astype('uint32')
    boards = []
    for board in data[1:]:
        board_nums = [int(o) for o in board.replace('\n', ' ').split()]
        board_nums = np.array(board_nums).reshape((5, 5))
        boards.append(board_nums)
    boards = np.stack(boards).astype('int32')
    return numbers, boards


def check_boards(nums, boards):
    pick = None
    for pick, num in enumerate(nums):
        boards[(boards == num)] = -1
        for board in boards:
            is_bingo = np.any([
                board.sum(axis=0) == -5,
                board.sum(axis=1) == -5,
            ])
            if is_bingo:
                board[(board == -1)] = 0
                result = num * board.sum()
                return pick, result
    return pick, None


def part1(fname):
    nums, boards = get_data(fname)
    print(check_boards(nums, boards)[1])


def part2(fname):
    nums, boards = get_data(fname)
    last = None
    for idx in range(len(boards)):
        val = check_boards(nums, boards[idx:idx+1])
        if not last or val[0] > last[0]:
            last = val
    print(last[1])


# part1('input_test.txt')
# part1('input.txt')
# part2('input_test.txt')
part2('input.txt')
